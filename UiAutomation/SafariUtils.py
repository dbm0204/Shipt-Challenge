""" Author:         Ben Mathew, Email: dbm0204@gmail.com
    Description:    The project is to use Selenium Webdriver to 
                    test
    Version:        1.0
    Compiler:       Python 3.X
    Python Package: Selenium 3.141.0 """
"""The below lines indicate the import statements"""
import os
import random
import string
from DriverUtils import driverUtils
from selenium import webdriver

class SafariUtils(driverUtils):
    #Default constructor
    def __init__(self):
        #instantiate an instance of driverUtils
        driverUtils.__init__(self)
        #Set the driver name
        self.set_driver_name("safaridriver")
        #Utility variable to get the path of the safaridriver.
        chrome_location = os.path.dirname(os.path.abspath(__file__))
        #Setting the path of the driver
        self.set_driver_path(os.path.join(chrome_location,self.get_driver_name()))
        #Instantiating an instance of the browser object.
        self.browser = webdriver.Chrome(executable_path=self.driver_path)

    #Getter function for safari driver session
    def getBrowser(self):
        return self.browser

    #Setter function for safari Driver session
    def setBrowser(path):
        try:
            self.browser = WebDriver(executable_path=path)
        except Exception as e:
            print(str(e))
