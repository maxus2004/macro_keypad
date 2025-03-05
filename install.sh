sudo pip install -r requirements.txt --break-system-packages

sudo mkdir /opt/seltech-keypad
sudo mkdir /opt/seltech-keypad/images

sudo cp images/tray_bluetooth.png /opt/seltech-keypad/images/tray_bluetooth.png
sudo cp images/tray_disconnected.png /opt/seltech-keypad/images/tray_disconnected.png
sudo cp images/tray_usb.png /opt/seltech-keypad/images/tray_usb.png
sudo cp images/icon.png /opt/seltech-keypad/images/icon.png

sudo cp keypad_daemon.py /opt/seltech-keypad/keypad_daemon.py
sudo cp keypad_gui.py /opt/seltech-keypad/keypad_gui.py
sudo cp ui_main_window.py /opt/seltech-keypad/ui_main_window.py
sudo cp ui_key_action_settings.py /opt/seltech-keypad/ui_key_action_settings.py

sudo cp config.json /opt/seltech-keypad/config.json
sudo chown $USER:$USER /opt/seltech-keypad/config.json

sudo cp seltech-keypad.service /etc/systemd/system/seltech-keypad.service
sudo systemctl enable seltech-keypad
sudo systemctl restart seltech-keypad

sudo cp seltech-keypad-gui.service /etc/systemd/user/seltech-keypad-gui.service
systemctl enable --user seltech-keypad-gui
systemctl restart --user seltech-keypad-gui

cp seltech-keypad-gui.desktop ~/.local/share/applications/seltech-keypad-gui.desktop

echo DONE!