class TestCaseOne():
    def __init__(self,utils):
        self.utils= utils
        self.driver = self.utils.getDriver()

    def test_setup(self):
        self.utils.goToUrl("https://www.serebii.net")
        self.driver.set_page_load_timeout(1000)

    def test_clean_up(self):
        print("LOG: Clean-up activites initiated")

    def test_end_test(self):
        print("LOG: Exiting TestCase Launch")
        self.driver.quit()
