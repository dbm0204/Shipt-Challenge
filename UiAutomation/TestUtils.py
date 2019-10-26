"""
Author:     Ben Mathew , Email:dbm0204@gmail.com
Project:    UI test on shipt.com using UI automation
            tools like Selenium for Chrome, Firefox 
            and Safari.
Compiler:   Python 3.X"""
"""Importing modules"""
from FireFoxUtils  import FireFoxUtils
from ChromeUtils import ChromeDriverUtils
from SafariUtils import SafariUtils

""" TestUtils is a class that instantiates an instance 
    of the browser(chrome,firefox,safari)"""
class TestUtils():
    """class method that instaniates an instance of 
        the browser."""
    def __init__(self,browser="chrome",link=None):
        try:
            #Sets the link to be naviageted
            self.link =link
            #Checks if the browser to be instantiated 
            #is firefox
            if browser == "firefox":
                #Instaniates an instance of the firefox 
                #Browser
                fox = FireFoxUtils()
                #Sets an instance of the firefox driver
                self.driver = fox.getBrowser()
            #Checks if the browser to be instanaites is 
            #Chrome
            elif browser == "chrome":
                #Instaniates an instance of the chrome 
                #browser
                chrome = ChromeDriverUtils()
                #Instaniates an instance of the chrome
                #driver
                self.driver = chrome.getBrowser()
            #Checks if the browser to be instantiated is 
            #safari
            elif browser =="safari":
                #Instaniates an instance og the Safaru browser
                safari = SafariUtils()
                #Instantiates an instance of the safari browser
                self.driver = safari.getBrowser()
        except Exception as e:
            print(str(e))
    """Getter function for the driver associated to the browser"""
    def getDriver(self):
        return self.driver

    """ Setter function for the driver assocayed to the browser"""
    def setDriver(self,driver):
        self.driver= driver
    
    """ Setter function for the link to be navigated"""
    def set_link(self,link):
        self.link=link
    
    """ Getter function for the Link to be navigated"""
    def get_link(self):
        return self.link
    
    """Function that lets the browser navigates to the specified
        link"""
    def goToUrl(self,link):
        try:
            #Browser fetches the webpage specified in the link.
            self.driver.get(link)
        except Exception as e:
            print("ERROR:Failed to load URL\n"+str(e))
