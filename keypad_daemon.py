import serial_asyncio
from ble_serial.bluetooth.ble_client import BLE_client
import asyncio
import keyboard
import pyperclip
import os.path
import logging
import traceback
import time

usb_connected = False
ble_connected = False


def type_str(str):
    prev_clipboard = pyperclip.paste()
    pyperclip.copy(str)
    time.sleep(0.01)
    keyboard.send("shift+insert")
    time.sleep(0.01)
    pyperclip.copy(prev_clipboard)


def process_message(command_str):
    event_type = command_str[0]
    key_id = int(command_str[1::])

    if event_type == "P":
        match key_id:
            case 4:
                if keyboard.is_pressed("shift"):
                    type_str("\\Alpha ")
                else:
                    type_str("\\alpha ")
            case 3:
                if keyboard.is_pressed("shift"):
                    type_str("\\Delta ")
                else:
                    type_str("\\delta ")
            case 2:
                if keyboard.is_pressed("shift"):
                    type_str("\\Lambda ")
                else:
                    type_str("\\lambda ")
            case 1:
                type_str("\\forall ")
            case 9:
                type_str("\\in ")
            case 8:
                type_str("\\exists ")


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

        await asyncio.sleep(1)


ble_buffer = ""


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
            while ble.dev.is_connected:
                if usb_connected:
                    await ble.disconnect()
                await asyncio.sleep(1)
        except Exception as e:
            if (
                e.args != ("No matching device found!",)
                and e.args != ("failed to discover services, device disconnected",)
                and not isinstance(e,EOFError)
            ):
                traceback.print_exc()

        if ble_connected:
            ble_connected = False
            print("BLE disconnected")

        await asyncio.sleep(1)


async def main():
    logging.basicConfig(level=logging.ERROR)
    await asyncio.gather(ble_loop(), usb_loop())


asyncio.run(main())
