""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""    

"""Import Statements"""
import time
import sys
import traceback
from TestSuiteContainer import TestSuiteContainer
from TestUtils import TestUtils
from TestCaseTwo import TestCaseTwo
from TestCaseOne import TestCaseOne
from ExecuteTestCaseOne import ExecuteTestCaseOne
from ExecuteTestCaseTwo import ExecuteTestCaseTwo

""" TestRunner is a class that takes an testcase from 
    the testsuiteContainer and executes the test.
    It inherits properties from TestSuiteContainer."""
class TestRunner(TestSuiteContainer):
    """ Class Method that instaniates porperties of 
        objects of type TestRunner."""
    def __init__(self,browser=None):
        #Instantiates an object of TestSuiteContainer.
        TestSuiteContainer.__init__(self)
        #Instantiates an instance of the browser.
        self.browser= browser
        #Instantiats an instance of TestUtils.
        self.testUtils = TestUtils(browser)
    
    """ browser_init() reinitiates the session of the browser 
        before a given test. """
    def browser_init(self):
        #Instaniates an instance fo the browser.
        self.testUtils = TestUtils(self.browser)
    
    """ browser_delete() deletes the current session of the 
        browser"""
    def browser_delete(self):
        #Deallocates the current instance of the browser.
        del(self.testUtils)
    
    """Getter function for TestUtils"""
    def get_test_utils(self):
        return self.testUtils

    """Settter function for TestUtils"""
    def set_test_utils(self,browser):
        self.testUtils = TestUtils(browser)
    
    """runs the test inputted to this function"""
    def run_test(self,l1):
        #Appends the testcase to the Queue.
        self.queue.append(l1)
        #Logs the message
        print("Metadata of Test:\n"+str(self.queue))
        #Pops the testCase from the queue and exeutes it.
        self.execute_from_rear() 
"""
main() is a function that test the functionalites implemented
in TestRunner.
"""
def main():
    try:
        #Lgogging Message
        print("-"*100)
        #Instanitiates an instance of TestRunner with chrome Browser
        runner = TestRunner("chrome")
        #Creates an instance of TestCaseOne
        t1 = TestCaseOne(runner.get_test_utils())
        #Creates an instance of ExecuteTEstCaseOne
        execTest1 = ExecuteTestCaseOne(t1)
        #Executes the testCase
        runner.run_test(execTest1)
        #Deletes an instance of the browser.
        runner.browser_delete()
        
        #Logging Message
        print("-"*100)
        #Reinitalizes the instance of the browser
        runner.browser_init()
        #Creates an instance of Type TesrCaseTwo
        t2 = TestCaseTwo(runner.get_test_utils())

        #Creates an instance fo Type ExecuteTestCaseTwo
        execTest2 = ExecuteTestCaseTwo(t2)
        #Sets the webdriver instance to sleep for 10 seconds
        time.sleep(10)
        #Executes the TestCase
        runner.run_test(execTest2)
        #Deletes an instance of the browser.
        runner.browser_delete()
    except Exception as e:
        #Lgogging Message
        print("Exception in user code:")
        #Logging Message
        print("-"*60)
        #Prints the stack trace.
        traceback.print_exc(file=sys.stdout)
        #Logging Message,
        print("-"*60)

if __name__=='__main__':
    main()
