import serial_asyncio
from ble_serial.bluetooth.ble_client import BLE_client
import asyncio
import keyboard
import pyperclip
import os.path
import logging
import traceback
import time
import socket
import json
from threading import Thread

usb_connected = False
ble_connected = False
ipc_connected = False
ipc_connection = None

ble_buffer = ""

layout_id = "layout1"
pressed_keys = []

config = json.load(open("config.json", "rb"))

def type_str(str):
    prev_clipboard = pyperclip.paste()
    pyperclip.copy(str)
    time.sleep(0.01)
    keyboard.send("ctrl+v")
    time.sleep(0.01)
    pyperclip.copy(prev_clipboard)


def process_message(command_str):
    event_type = command_str[0]
    key_id = str(int(command_str[1::])+1)

    if key_id not in config["actions"][layout_id]: return
    
    if event_type == "P":
        pressed_keys.append(key_id)
        for action in config["actions"][layout_id][key_id]:
            if "action" not in action: continue

            if "modifiers" in action:
                modifiers_correct = True
                for modifier_key in action["modifiers"]:
                    if modifier_key.startswith("btn_"):
                        if(modifier_key[4::] not in pressed_keys): 
                            modifiers_correct = False
                            break
                    elif not keyboard.is_pressed(modifier_key):
                        modifiers_correct = False
                        break
                if not modifiers_correct: continue

            if action["action"] == "type":
                type_str(action["str"])
            elif action["action"] == "cmd":
                os.system(action["cmd"])

            break

    elif event_type == "R":
        pressed_keys.remove(key_id)


async def usb_loop():
    print("USB loop started")
    global usb_connected
    while True:
        while not os.path.exists("/dev/ttyACM0"):
            await asyncio.sleep(1)

        try:
            usb_reader, usb_writer = await serial_asyncio.open_serial_connection(
                url="/dev/ttyACM0"
            )
            usb_connected = True
            print("USB connected")
            update_status()
            while True:
                line = (await usb_reader.readuntil(b"\n")).decode().strip()
                process_message(line)
        except Exception as e:
            if e.args != (
                "device reports readiness to read but returned no data (device disconnected or multiple access on port?)",
            ):
                traceback.print_exc()

        if usb_connected:
            usb_connected = False
            print("USB disconnected")
            update_status()

        await asyncio.sleep(1)


def ble_receiver(bytes):
    global ble_buffer
    ble_buffer += bytes.decode()
    messages = ble_buffer.split("\r\n")
    ble_buffer = messages.pop()
    for message in messages:
        process_message(message)


async def ble_loop():
    print("BLE loop started")
    global ble_connected
    ble = BLE_client("hci0", "ID")
    ble.set_receiver(ble_receiver)
    while True:
        while usb_connected:
            await asyncio.sleep(1)

        try:
            await ble.connect("12:34:56:01:E0:D2", "public", None, 10.0)
            await ble.setup_chars(None, None, "rw", True)
            if usb_connected:
                await ble.disconnect()
                continue
            ble_connected = True
            print("BLE connected")
            update_status()
            while ble.dev.is_connected:
                if usb_connected:
                    await ble.disconnect()
                await asyncio.sleep(1)
        except Exception as e:
            if (
                e.args != ("No matching device found!",)
                and e.args != ("failed to discover services, device disconnected",)
                and e.args != ('org.bluez.Error.NotReady', 'Resource Not Ready',)
                and not isinstance(e,EOFError)
            ):
                print(e.args)
                traceback.print_exc()

        if ble_connected:
            ble_connected = False
            print("BLE disconnected")
            update_status()
        await asyncio.sleep(1)

    
def update_status():
    global ipc_connection, ipc_connected
    if not ipc_connected: return
    try:
        ipc_connection.sendall(json.dumps({"usb_connected":usb_connected,"ble_connected":ble_connected}).encode())
    except BrokenPipeError: 
        ipc_connected = False


def ipc_loop():
    global ipc_connection, config, ipc_connected
    print('IPC loop started')
    try:
        os.unlink('/run/seltech-keypad.sock')
    except OSError:
        if os.path.exists('/run/seltech-keypad.sock'):
            raise

    server = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)
    server.bind('/run/seltech-keypad.sock')
    os.chmod("/run/seltech-keypad.sock" , 0o777)

    server.listen(1)

    while True:
        ipc_connection, _ = server.accept()

        try:
            print("IPC client connected")
            ipc_connected = True

            update_status()
            while True:
                data = ipc_connection.recv(1024)
                if not data:
                    break
                command = data.decode()
                if command=="reload_config":
                    config = json.load(open("config.json", "rb"))
        except ConnectionResetError:
            pass
        print("IPC client disconnected")
        ipc_connected = False


async def main():
    logging.basicConfig(level=logging.ERROR)
    Thread(target=ipc_loop).start()
    await asyncio.gather(ble_loop(), usb_loop())


asyncio.run(main())
