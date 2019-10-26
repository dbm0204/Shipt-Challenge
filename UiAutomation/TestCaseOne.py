""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X 
    Python Packages:    Selenium 3.141.0"""    

"""
TestCaseOne is a class that contains the follwing methods 
necessary to execute an instance of the class.
    test_setup:     Sets uf the necessary preconditions for the test
    test_main:      Performs the test
    test_clean:     Performs the clean after the test is over
    test_exit:      Deletes the instance of the test and the browser
"""
class TestCaseOne():
    
    """ Class Method that instaniates an instance of 
        TestCaseOne. The properties of an object of TestCaseOne
        include utils( which is an instance of TestUtils) and 
        driver( which is a instance of the driver on which the 
        test in being run on"""
    def __init__(self,utils,name=None,desc=None):
        #Initiates an instance of TestUtil
        self.utils= utils
        #gets an instance of the browser to run the test.
        self.driver = self.utils.getDriver()
    
    """ test_setup is a method that sets up the necessary preconditions 
        necessary to perform the test."""
    def test_setup(self):
        #Navigates to the url inorder to run the tetst
        self.utils.goToUrl("https://www.serebii.net")
        #Sets the page load timeout to 1000 seconds
        self.driver.set_page_load_timeout(1000)

    """test_main is a method that executes the test"""
    def test_main(self):
        pass
    """ test_clean is a method that performs clean up activities 
        after the test."""
    def test_clean(self):
        print("LOG: Clean-up activites initiated")
        self.driver.close()
    
    """test_exit is a method that exits the session of the browser 
        and closes the browser."""
    def test_exit(self):
        print("LOG: Exiting TestCase Launch")
        self.driver.quit()
