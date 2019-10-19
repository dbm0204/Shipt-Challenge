"""
Author:     Ben Mathew , Email:dbm0204@gmail.com
Project:    UI test on shipt.com using UI automation
            tools like Selenium for Chrome, Firefox 
            and Safari.
Compiler:   Python 3.X

"""
import os
from FirefoxUtils import FireFoxUtils
from FirefoxUtils import ChromeDriverUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
class TestUtils():

    def __init__(self,browser="chrome"):
        if browser == "firefox":
            fox = FireFoxUtils()
            self.driver = fox.getBrowser()
            
        elif browser == "chome":
            chrome = ChromeDriverUtils()
            self.driver = chrome.getBrowser()

    def getDriver(self):
        return self.driver

    def setDriver(self,driver):
        self.driver= driver

    def goToUrl(self,link):
        try:
            self.driver.get(link)
        except Exception as e:
            print("ERROR:Failed to load URL\n"+str(e))
    
    def test_shopping_chart(self):
        try:
            self.goToUrl("www.https://shop.shipt.com/")
            self.driver.set_page_load_timeout(10)

        except Exception as e:
            print("Error:")
            print(str(e))


def main():
    utils = TestUtils()
    utils.test_shopping_chart()


if __name__=='__main__':
    main()

