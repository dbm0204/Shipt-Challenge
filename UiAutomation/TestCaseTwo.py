class TestCaseTwo():
    def __init__(self,utils):
        self.utils = utils
        self.driver = self.utils.getDriver()

    def test_setup(self):
        print("LOG: Navigating to Facebook")
        self.utils.goToUrl("https://www.facebook.com")

    def test_execute(self):
        print("PRINT:Executing Facebook Test Case:")

    def test_clean(self):
        print("LOG:Clean-up activities initiated")

    def test_exit(self):
        print("LOG: Test is being exited")
