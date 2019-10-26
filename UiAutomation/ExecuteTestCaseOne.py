""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""    


import sys, traceback
from ExecuteTestCase import ExecuteTestCase
from TestCaseOne import TestCaseOne
from TestUtils import TestUtils

class ExecuteTestCaseOne(ExecuteTestCase):
    def __init__(self,testOne):
        self.testOne = testOne
    
    def __str__(self):
        print(self.testOne)

    def execute(self):
        try:
            self.testOne.test_setup()
            self.testOne.test_main()
            self.testOne.test_clean()
            self.testOne.test_exit()
        except Exception as e:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
    def get_test_case(self):
        return self.testOne
