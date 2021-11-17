from playsound import playsound
from time import sleep
import RPi.GPIO as GPIO
import configparser
import tplink
import os

chromedriverpath = parser.get("config", "chromedriverpath")
backupfilepath = parser.get("config", "backupfilepath")
adminip = parser.get("config", "adminip")
ip = parser.get("config", "ip")
pwd = parser.get("config", "pwd")

def isAlive(ip):
    response = os.system("ping -w 1 " + ip + " >/dev/null 2>&1")
    if response == 0:
        playsound('pull-out-551.mp3')
        return True
    else:
        return False
        
tp = tplink.Tplink(chromedriverpath, backupfilepath, ip, pwd)

while True:
    if isAlive(ip):
        try:
            tp.setUp(chromedriverpath)
            tp.setPwd("http://" + ip, pwd)
            tp.login("http://" + ip, pwd)
            tp.uploadBackupFile(backupfilepath)
        except:
            tp.exit()
        finally:
            tp.exit()
    elif isAlive(adminip):
        playsound('pull-out-551.mp3')
        playsound('pull-out-551.mp3')
    else:
        print("waiting")
    sleep(5)

    
