from TestCase import TestCase
from TestCaseOne import TestCaseOne
from TestUtils import TestUtils

class LaunchTestCaseOne(TestCase):
    def __init__(self,testOne):
        self.testOne = testOne

    def execute(self):
        self.testOne.test_setup()
        self.testOne.test_clean_up()
        self.testOne.test_end_test()
