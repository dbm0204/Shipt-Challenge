""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""
import sys, traceback
from TestUtils import TestUtils
from TestCaseTwo import TestCaseTwo
from ExecuteTestCase import ExecuteTestCase

class ExecuteTestCaseTwo(ExecuteTestCase):
    def __init__(self, testTwo):
        self.testTwo = testTwo

    def __str__(self):
        print(self.testTwo)

    def execute(self):
        try:
            print("LOG: Test Setup Initiated")
            self.testTwo.test_setup()
            print("LOG: Test Main Initiated")
            self.testTwo.test_main()
            print("LOG: Test Cleanup Initiated")
            self.testTwo.test_clean()
            print("LOG: Test Exit Initiated ")
            self.testTwo.test_exit()
        except Exception as e:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
    
    def get_test_case(self):
        return self.testTwo
