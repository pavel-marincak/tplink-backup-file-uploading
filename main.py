import tplink

class main:

    if __name__ == "__main__":
        chromedriverpath = "chromedriver/chromedriver95"
        backupfilepath = "/home/mari/Documents/projects/tplink-backup-file-uploading/backupfile/EC230-G1V121022628368n.bin"
        adminip = "admin ip"
        ip = "default rtr ip"
        pwd = "rtr pwd"
        ssid = None
        wifipwd = None
        

        tp = tplink(chromedriverpath, backupfilepath, ip, pwd)