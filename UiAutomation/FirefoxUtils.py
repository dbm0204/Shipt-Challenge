import os
import random
import string
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class FireFoxUtils():
    def __init__(self):
        gecko_location = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(gecko_location,"geckodriver") 
        self.binary = FirefoxBinary(self.file_path)
        self.caps = DesiredCapabilities.FIREFOX.copy()
        self.caps['marionette'] = False
        options =Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        self.browser = webdriver.Firefox(firefox_binary=self.binary,
                                         capabilities=self.caps,
                                         options=options)

    def getBrowser(self):
        return self.browser

    def setBrowser(self, binary):
        self.browser = Firefox(binary)

    def KillBrowser(self):
        self.browser.kill()

    def get_file_path(self):
        return self.file_path
    
    def getCapabilities(self):
        return self.caps

class ChromeDriverUtils():
    
    def __init__(self):
        chrome_location = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(chrome_location,"chromedriver")
        self.browser = webdriver.Chrome(executable_path=self.file)

    def getBrowser(self):
        return self.browser

    def setBrowser(path):
        self.browser = WebDriver(executable_path=path)


    def KillBrowser(self):
        self.browser.quit()

    def get_file_path(self):
        return self.file

def main():
    chrome = ChromeDriverUtils()
    driver = chrome.getBrowser()
    driver.implicitly_wait(10)
    driver.get("https://shop.shipt.com/login")
    driver.set_page_load_timeout(160)
    driver.find_element_by_id("username").send_keys("dbm0204@gmail.com")
    driver.find_element_by_id("password").send_keys("deepu0402!")
    elementList = driver.find_elements_by_class_name("button-1")
    elementList[2].click()
    driver.set_page_load_timeout(250)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/header/div/a[1]').click()
    driver.set_page_load_timeout(300)
    driver.find_elements_by_class_name("button-1")[0].click()
    driver.set_page_load_timeout(30)
    driver.find_element_by_id("adr-street1").send_keys("ASDFZXC")
    driver.find_element_by_id("adr-state").send_keys("ASD")
    driver.find_element_by_id("adr-city").send_keys("QWERTY")
    driver.find_element_by_id("adr-zip").send_keys("94014")
    driver.find_elements_by_class_name("fwCDEt")[0].click()
    driver.set_page_load_timeout(40000)
    driver.save_screenshot('screenie.png')
    print("Test Completed")


if __name__ == "__main__":
    main()
