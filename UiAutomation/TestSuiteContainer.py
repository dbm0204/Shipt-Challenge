""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""    

"""Import Statement"""
import time
import sys
import traceback
from TestCaseOne import TestCaseOne
from TestCaseTwo import TestCaseTwo
from TestUtils import TestUtils
from collections import deque
from ExecuteTestCaseOne import ExecuteTestCaseOne
from ExecuteTestCaseTwo import ExecuteTestCaseTwo

""" TestSuiteContainer is the container class for the testcases.
    objects of this class has a queue as a property. This Qeueue
    keeps track of the testcases that needs to be executed."""
class TestSuiteContainer():
    """Class Method that instaniates objects with the
        properties."""
    def __init__(self):
        self.queue = deque()
    """Append is a method that appends the testCases to the 
        queue"""
    def append(self,testCase):
        self.queue.append(testCase)

    """Getter function for the Queue of testCases.  """
    def get_queue(self):
        return self.queue

    """Return the testcase at a perticular index of the queue"""
    def get_test_by_index(self,index):
        try:
            return self.queue[index]
        except Exception as e:
            print(str(e))

    """Returns the first testcase from the front of the queue."""
    def from_front(self):
        try:
            """If the queue is Empty Log the message"""
            if len(self.queue)== 0:
                print("ERROR: The Queue is Empty")
            #Else return the first TestCase in the Queue
            elif len(self.queue)>0:
                return self.queue.popleft()
        except Exception as e:
            print(str(e))
    """Executes the last testcase from the rear of the queue"""
    def execute_from_rear(self):
        #Assigns the testcase to be executed
        temp = self.fron_front()
        #Executees the testcase.
        temp.execute()
    
    """Returns the last testcase in the queue"""
    def from_rear(self):
            #If the queue is empty then log an error message
            if len(self.queue)==0:
                print("ERROR: The Queue is Empty")
            #If the list is not empty then retuen the last element.
            elif len(self.queue)>0:
                return self.queue.pop()

    """Executes the testcase returned by from_rear"""
    def execute_from_rear(self):
        #Assigns the testcase returned from the rear of the queue
        temp = self.from_rear()
        #Executes the testcase
        temp.execute()


def run_test(l1):
    try:
        #Instantiates an instance of TestRunner
        runList = TestRunner()
        #Appends the testcase of the queue
        runList.append(l1)
        #Logging message 
        print("Metadata of Test:\n"+str(runList.queue))
        #Executing the process from the rear.
        runList.execute_from_rear()
    except Exception as e:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
