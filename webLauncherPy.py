import sys
import ctypes
import configparser

def getdomain(url):
    return 0


def main(argv):
    ctypes.windll.user32.MessageBoxW(0, "sup dude", "title", 1)
    config = configparser.ConfigParser()
    config.read("webLauncherPy.ini")

    browser1 = config.get("Browsers", "Browser1", fallback="iexplore.exe")
    browser2 = config.get("Browsers", "Browser2", fallback="chrome.exe")
    domains1 = config.get("Domains", "Domains1", fallback="ukwdc-qcapp1:8080")

    ctypes.windll.user32.MessageBoxW(0, "Browser1="+browser1,"title",1)

if __name__ == "__main__":
	main(sys.argv[1:])