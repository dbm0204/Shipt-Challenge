from TestUtils import TestUtils
from TestCaseTwo import TestCaseTwo

class LaunchTestCaseTwo():
    def __init__(self, testTwo):
        self.testTwo = testTwo

    def execute(self):
        self.testTwo.test_setup()
        self.testTwo.test_clean()
        self.testTwo.test_exit()
