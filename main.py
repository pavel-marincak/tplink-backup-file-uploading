from time import sleep
import RPi.GPIO as GPIO
import configparser
import tplink
import os

parser = configparser.ConfigParser()
parser.read("config.txt")

chromedriverpath = parser.get("config", "chromedriverpath")
backupfilepath = parser.get("config", "backupfilepath")
adminip = parser.get("config", "adminip")
ip = parser.get("config", "ip")
pwd = parser.get("config", "pwd")

buzzerPIN = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPIN,GPIO.OUT)
buzz = GPIO.PWM(buzzerPIN, 1000)

def buzzer(i):
    for i in range(0,i):
        buzz.start(50)
        sleep(0.05)
        buzz.stop()
        sleep(0.05)

def isAlive(ip):
    response = os.system("ping -w 1 " + ip + " >/dev/null 2>&1")
    if response == 0:
        buzzer(1)
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
            buzzer(5)
        finally:
            tp.exit()
    elif isAlive(adminip):
        buzzer(2)
    else:
        print("waiting")
    sleep(5)

    
