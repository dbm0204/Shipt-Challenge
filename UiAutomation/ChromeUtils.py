""" Author:         Ben Mathew, Email: dbm0204@gmail.com
    Description:    The project is to use Selenium Webdriver to test
    Version:        1.0
    Compiler:       python 3.X
    Python Package: Selenium 3.141.0"""

"""The below lines indicate the import statements"""
import os
import random
import string
from DriverUtils import driverUtils
from selenium import webdriver

"""ChromeDriverUtils is a class that contains 
the utility functions (i.e. getter and setter functions
and memeber variables(i.e. the path to the chrome driver)."""

class ChromeDriverUtils(driverUtils):    
    #Default constructor
    def __init__(self):
        #instatiate an instance of driverUtils
        driverUtils.__init__(self)
        #Set the driver name
        self.set_driver_name("chromedriver")
        #Utilty variable to get the path of the chromedriver
        chrome_location = os.path.dirname(os.path.abspath(__file__))
        #Setting the path of the driver
        self.set_driver_path(os.path.join(chrome_location,self.get_driver_name()))
        #Instantiating an instance of the browser object.
        chrome_options = webdriver.ChromeOptions()
        #Sets crome to incognito mode
        chrome_options.add_argument("--incognito")
        #sets chrome to full screeen mode
        chrome_options.add_argument("--kiosk")
        #Instaniates an instance of the chrome browser with the above options
        self.browser = webdriver.Chrome(executable_path=self.driver_path,
                                        chrome_options=chrome_options)

    #Getter function for chrome driver session
    def getBrowser(self):
        return self.browser

    #Setter finction for chrome driver session
    def setBrowser(path):
        self.browser = WebDriver(executable_path=path)
