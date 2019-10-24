""" Author:         Ben Mathew, Email: dbm0204@gmail.com
    Description:    The project is to use Selenium Webdriver to test
    Version:        1.0
    compiler:       python 3.X
    Python Package: selenium 3.141.0"""

#Import statements
import os
import random
import string
from DriverUtils import driverUtils
from selenium import webdriver

class FireFoxUtils(driverUtils):
    def __init__(self):
        #Instantiate a instance of gekodriver
        driverUtils.__init__(self)
        #set teh driver name
        self.set_driver_name("gekodriver")
        #Utility variable to get the path of the gekoDriver
        chrome_location = os.path.dirname(os.path.abspath(__file__))
        #Setting the path of the driver
        self.set_driver_path(os.path.join(chrome_location,self.get_driver_name()))
        #Instantiating an instance of the browser object.
        self.browser = webdriver.Chrome(executable_path=self.driver_path)

    #Getting an instance of the browser sesstion
    def getBrowser(self):
        return self.browser

    #Setting an instance of the browser session
    def setBrowser(path):
        self.browser = WebDriver(executable_path=path)

