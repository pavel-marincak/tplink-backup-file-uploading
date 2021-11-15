import tplink
import os

chromedriverpath = "chromedriver/chromedriver95"
backupfilepath = "/home/mari/Documents/projects/tplink-backup-file-uploading/backupfile/EC230-G1V121022628368n.bin"
adminip = "admin ip"
ip = "default rtr ip"
pwd = "rtr pwd"

def isAlive(ip):
    response = os.system("ping -w 1 " + ip + " >/dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

tp = tplink.Tplink(chromedriverpath, backupfilepath, ip, pwd)
tp.setUp(chromedriverpath)``

while True:
    if isAlive(ip):
        try:
            tp.setUp(chromedriverpath)
            tp.setPwd(ip, pwd)
        except:
            tp.exit()
