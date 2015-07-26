import sys
import ctypes
import configparser
from subprocess import Popen

def getdomain(url):
    url = url.split("//")[1]
    url = url.split("/")[0]
    return str(url)

def main(argv):

    config = configparser.ConfigParser()
    config.read("webLauncherPy.ini")

    browser1 = config.get("Browsers", "Browser1", fallback="iexplore.exe")
    browser2 = config.get("Browsers", "Browser2", fallback="chrome.exe")
    domains1 = config.get("Domains", "Domains1", fallback="ukwdc-qcapp1:8080")

    domain = getdomain(argv[0])
    ctypes.windll.user32.MessageBoxW(0, domain,"title",0)

    if domain in domains1:
    	browserToRun = browser1
    else:
    	browserToRun = browser2

    p = Popen(browserToRun, argv[0])
    
if __name__ == "__main__":
	main(sys.argv[1:])