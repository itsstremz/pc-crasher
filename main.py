import os
import pyautogui
import subprocess

while True:
    os.system("start")
    pyautogui.write('lollololol')
    pyautogui.hotkey('esc')
    subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
    subprocess.call(['C:\Program Files\Google\Chrome\Application\\chrome.exe'])
    subprocess.call(['C:\Program Files\Internet Explorer\\iexplore.exe'])
