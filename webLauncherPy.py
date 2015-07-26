import sys
import ctypes
import configparser

ctypes.windll.user32.MessageBoxW(0, "sup dude", "title", 1)
config = configparser.ConfigParser()
config.read(webLauncherPy.ini)

browser1 = config.get("Browsers", "Browser1", fallback="iexplore.exe")

browser2 = config.get("Browsers", "Browser2", fallback="chrome.exe")

browser3 = 