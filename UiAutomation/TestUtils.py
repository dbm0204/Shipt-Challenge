"""Author:     Ben Mathew , Email:dbm0204@gmail.com
Project:    UI test on shipt.com using UI automation
            tools like Selenium for Chrome, Firefox 
            and Safari.
Compiler:   Python 3.X
"""
from FireFoxUtils  import FireFoxUtils
from ChromeUtils import ChromeDriverUtils
from SafariUtils import SafariUtils
class TestUtils():

    def __init__(self,browser="chrome",link=None):
        try:
            self.link =link
            if browser == "firefox":
                fox = FireFoxUtils()
                self.driver = fox.getBrowser()
            
            elif browser == "chrome":
                chrome = ChromeDriverUtils()
                self.driver = chrome.getBrowser()
        
            elif browser =="safari":
                safari = SafariUtils()
                self.driver = safari.getBrowser()
        
        except Exception as e:
            print(str(e))

    def getDriver(self):
        return self.driver

    def setDriver(self,driver):
        self.driver= driver
    
    def set_link(self,link):
        self.link=link

    def get_link(self):
        return self.link

    def goToUrl(self,link):
        try:
            print(link)
            self.driver.get(link)
        except Exception as e:
            print("ERROR:Failed to load URL\n"+str(e))
