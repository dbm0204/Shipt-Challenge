"""
Author:     Ben Mathew , Email:dbm0204@gmail.com
Project:    UI test on shipt.com using UI automation
            tools like Selenium for Chrome, Firefox 
            and Safari.
Compiler:   Python 3.X

"""
import os
import unititest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
class TestUtils():

    def __init__(self,browser="chrome"):
        if browser == "firefox":
            package_dir = os.path.dirname(os.path.abspath(__file__))
            firefox_bin = os.path.join(package_dir,"geckodriver")
            self.fireFox_binary = FirefoxBinary(firefox_bin)
            self.driver = webdriver.Firefox()
            
        elif browser == "chome":
            package_dir = os.path.dirname(os.path.abspath(__file__))
            firefox_bin = os.path.join(package_dir,"chromediver")
            self.driver = webdriver.Chrome()

    
    def getDriver(self):
        return self.driver

    def setDriver(self,driver):
        self.driver= driver

    def goToUrl(self,link):
        try:
            self.driver.get("www.shipt.com")
        except Exception as e:
            print("ERROR:Failed to load URL\n"+str(e))

