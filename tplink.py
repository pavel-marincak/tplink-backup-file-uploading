from selenium import webdriver
from time import sleep
import string
import os

class Tplink:
    def __init__(self, chromedriverpath, backupfilepath, ip, pwd):
        self.chromedriverpath = None
        self.backupfilepath = None
        self.ip = None
        self.pwd = None

    def setUp(self, chromedriverpath):
        self.driver = webdriver.Chrome(executable_path=chromedriverpath)
        self.driver.maximize_window()

    def exit(self):
        self.driver.quit()

    def setPwd(self, ip, pwd):
        self.driver.get(ip)
        print("page uploaded")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"pc-setPwd-new\"]").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id=\"pc-setPwd-confirm\"]").send_keys(pwd)
        save = self.driver.find_element_by_xpath("//*[@id=\"pc-setPwd-btn\"]/span")
        save.click()
        time.sleep(3)
        print("Password set")

    def login(self, ip, pwd):
        self.driver.get(ip)
        print("page uploaded")
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id=\"pc-login-password\"]").send_keys(pwd)
        login = self.driver.find_element_by_xpath("//*[@id=\"pc-login-btn\"]/span")
        login.click()
        print("Logged in")
        time.sleep(3)

    def uploadBackupFile(self, backupfilepath):
        advance = self.driver.find_element_by_xpath("//*[@id=\"advanced\"]/span[2]")
        advance.click()
        print("Advance")
        sleep(3)
        backup  = self.driver.find_element_by_xpath("//*[@id=\"menuTree\"]/li[10]/ul/li[5]/a")
        self.driver.execute_script("arguments[0].click();", backup)
        print("System tools >> Backup & Restore")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"filename\"]").send_keys(backupfilepath)
        print("File upload")
        time.sleep(5)
        restore = self.driver.find_element_by_xpath("//*[@id=\"t_restore\"]")
        restore.click()
        print("Restore")
        sleep(5)
        upload_chek = None
        while upload_chek != 100 :
            try:
                upload_chek = self.driver.find_element_by_xpath("//*[@id=\"gitem\"]").text
                upload_chek = upload_chek.replace("%", "")
                upload_chek = int(upload_chek)
                os.system("clear")
                print(upload_chek)
            except:
                upload_chek = 100
                print("eror")
        time.sleep(10)
    """
    def steWifi(self, ssid, wifipwd):
        wireless = self.driver.find_element_by_xpath("//*[@id=\"menuTree\"]/li[3]/a/span[2]")
        wireless.click()
        print("Wireless")
        time.sleep(3)
        #2,4G
        self.driver.find_element_by_xpath("//*[@id=\"ssid_2g\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"ssid_2g\"]").send_keys("GRAPE_" + ssid)
        self.driver.find_element_by_xpath("//*[@id=\"wpa2PersonalPwd_2g\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"wpa2PersonalPwd_2g\"]").send_keys(wifipwd)
        save_btn = self.driver.find_element_by_xpath("//*[@id=\"save_2g\"]/span")
        save_btn.click()
        time.sleep(10)
        print("2,4g set")

        #5G
        self.driver.find_element_by_xpath("//*[@id=\"ssid_5g\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"ssid_5g\"]").send_keys("GRAPE_" + ssid + "_5G")
        self.driver.find_element_by_xpath("//*[@id=\"wpa2PersonalPwd_5g\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"wpa2PersonalPwd_5g\"]").send_keys(wifipwd)
        save_btn = self.driver.find_element_by_xpath("//*[@id=\"save_5g\"]/span")
        save_btn.click()
        time.sleep(10)
        print("5g set")
        time.sleep(10)
        advance_btn = self.driver.find_element_by_xpath("//*[@id=\"advanced\"]/span[2]")
        advance_btn.click()
        print("Advance")
        time.sleep(5)
        mac = self.driver.find_element_by_xpath("//*[@id=\"macAddrV4\"]").get_attribute("value")
        ssid_check = self.driver.find_element_by_xpath("//*[@id=\"ssid_2g\"]").get_attribute("value")

        return mac, ssid_check, wifipwd
        """
