""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""
    

""" driverUtils is a POJO Class that contains 
the driver name and driver path as member variables. 
It also contains getter and settter functions for each of the
member variables.
"""
class driverUtils():
    """Class method for instantiating a object of type 
    driverUtils. The object driverUtils contains the driver name
    and driver path"""
    def __init__(self,name=None,path=None):
        self.driver = None
        self.driver_name = name
        self.driver_path = path

    """ Getter function for Driver"""
    def get_driver(self):
        return self.driver

    """ Setter Function for Driver"""
    def set_driver(self,driver):
        self.driver = driver

    """Gettter Functions for driver name"""
    def get_driver_name(self):
        return self.driver_name
    
    """Getter function for driver path"""
    def get_driver_path(self):
        return self.driver_path
    
    """Setter Function for driver name"""
    def set_driver_name(self, name):
        self.driver_name = name

    """Setter function for driver path"""
    def set_driver_path(self,path):
        self.driver_path = path
    
    """Method KillBrowser needs to be overridden in 
        inherited subclasses"""
    def kill_browser():
        self.driver.quit()


