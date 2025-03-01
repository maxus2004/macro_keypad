import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton, QDialog, QPlainTextEdit
from PySide6.QtGui import QIcon, QAction
from ui_main_window import Ui_mainWindow
from ui_key_action_settings import Ui_ButtonConfigDialog
import socket
from threading import Thread
import json

config = json.load(open("config.json", "rb"))

def toggleWindow(window: QMainWindow):
    if window.isVisible():
        window.close()
    else:
        window.show()

def save_settings():
    global ipc_client
    json.dump(config, open("config.json", "w"), indent=4)
    ipc_client.sendall("reload_config".encode())

def set_key_config(key_id:str, text_config:str):
    config["actions"]["layout1"][key_id] = []
    for line in text_config.split('\n'):
        if ':' not in line: continue
        modifiers_str = line.split(':')[0].strip()
        action_str = line.split(':')[1].strip()

        if action_str.startswith('"'):
            action_str = action_str[1:]
        if action_str.endswith('"'):
            action_str = action_str[:-1]

        action = {}
        if modifiers_str != "":
            action["modifiers"] = []
            for modifier in modifiers_str.split('+'):
                action["modifiers"].append(modifier)
        action["action"] = "type"
        action["str"] = action_str
        config["actions"]["layout1"][key_id].append(action)

def show_key_config(key_id: str, key: QPushButton):
    key_config_dialog = QDialog(window)
    key_config_dialog.ui = Ui_ButtonConfigDialog()
    key_config_dialog.ui.setupUi(key_config_dialog)
    key_config_dialog.ui.KeyCationTextEdit.setPlainText(key.text())
    def accept_action():
        key.setText(key_config_dialog.ui.KeyCationTextEdit.toPlainText())
        set_key_config(key_id, key_config_dialog.ui.KeyCationTextEdit.toPlainText())
    key_config_dialog.ui.buttonBox.accepted.connect(accept_action)
    key_config_dialog.show()
    key_config_dialog.ui.KeyCationTextEdit.selectAll()

def setup_settings_window():
    window = QMainWindow()
    window.ui = Ui_mainWindow()
    ui = window.ui
    ui.setupUi(window)
    ui.exit_btn.clicked.connect(app.quit)
    ui.cancel_btn.clicked.connect(window.close)
    ui.save_btn.clicked.connect(lambda: (save_settings(),window.close()))

    for i in range(20):
        key_id = str(i+1)
        key: QPushButton = ui.__dict__[f"key_{20-i}"]
        key.clicked.connect(lambda _, key_id=key_id, key=key: show_key_config(key_id,key))
        if key_id in config["actions"]["layout1"]:
            text = ""
            for action in config["actions"]["layout1"][key_id]:
                if "modifiers" in action: text += "+".join(action["modifiers"])
                text += ":\"" + action["str"] + "\"\n"
            key.setText(text)

    return window

def setup_tray(app, window):
    global settings_action, quit_action
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("images/tray_disconnected.png"))
    tray.activated.connect(lambda: toggleWindow(window))
    tray.setVisible(True)

    menu = QMenu()

    settings_action = QAction("Settings")
    settings_action.triggered.connect(lambda: toggleWindow(window))
    menu.addAction(settings_action)

    quit_action = QAction("Quit")
    quit_action.triggered.connect(app.quit)
    menu.addAction(quit_action)

    tray.setContextMenu(menu)
    return tray
    

def main():
    global ipc_client, app, window, tray
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    window = setup_settings_window()
    tray = setup_tray(app, window)
    Thread(target=ipc_loop).start()

    app.exec()
    ipc_client.shutdown(0)
    sys.exit(0)


def ipc_loop():
    global tray, ipc_client
    ipc_client = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)

    ipc_client.connect("/run/seltech-keypad.sock")

    while True:
        message_str = ipc_client.recv(1024).decode()
        if message_str == "": return
        data = json.loads(message_str)
        if data["usb_connected"]:
            tray.setIcon(QIcon("images/tray_usb.png"))
        elif data["ble_connected"]:
            tray.setIcon(QIcon("images/tray_bluetooth.png"))
        else:
            tray.setIcon(QIcon("images/tray_disconnected.png"))

main()