import time
from TestCaseOne import TestCaseOne
from TestCaseTwo import TestCaseTwo
from TestUtils import TestUtils
from LaunchTestCaseOne import LaunchTestCaseOne
from LaunchTestCaseTwo import LaunchTestCaseTwo
from collections import deque

class TestRunner():
    def __init__(self):
        self.queue = deque()
   
    def __str__(self):
        return str(self.queue)

    def append(self,command):
        self.queue.append(command)

    def get_queue(self):
        return self.queue

    def getElementByIndex(self,index):
        try:
            return self.queue[index]
        except Exception as e:
            print(str(e))

    def from_front(self):
        try:
            if len(self.queue)== 0:
                print("ERROR: The Queue is Empty")
            else:
                while len(self.queue)>0:
                    temp = self.queue.popleft()
                    temp.execute()
                    time.sleep(2)
        except Exception as e:
            print(str(e))

    def from_rear(self):
        try:
            if len(self.queue)==0:
                print("ERROR: The Queue is Empty")
            else:
                while len(self.queue)>0:
                    temp = self.queue.pop()
                    temp.execute()
                    time.sleep(10)

        except Exception as e:
            print(str(e))

def main():
    u1 = TestUtils(browser ="chrome")
    t1 = TestCaseOne(u1)

    u2 = TestUtils(browser ="chrome")
    t2 = TestCaseTwo(u2)
    
    l1 = LaunchTestCaseOne(t1)
    l2 = LaunchTestCaseTwo(t2)
    
    runList = TestRunner()
    runList.append(l1)
    runList.append(l2)        
    print(runList)
    runList.from_front()

if __name__=='__main__':
    main()
