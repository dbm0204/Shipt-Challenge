""" Author:             Ben Mathew, Email: dbm0204@gmail.com
    Description:        The project is to use Selenium Webdriver to test
    Version:            1.0
    Compiler:           Python 3.X
    Python Packages:    Selenium 3.141.0""" 
"""Import statements"""
import time

""" TestCaseTwo is a class that has the necessary methods to execute 
    testCaseTwo which is a the facebook test."""
class TestCaseTwo():
    """ Class Method to instantiate the properties of an 
        object of type TestCaseTwo"""
    def __init__(self,utils):
        #Instantiate an instance of TestUtils
        self.utils = utils
        #Gets the instance of the browser
        self.driver = self.utils.getDriver()
        #Creates an dictionary for the credentials
        self.credentials = dict()
    
    """ get_credential is getter function that gets the value 
        associated with a particular key"""
    def get_credentials(self,key):
        #Iterates through the keySet and returns the value
        if key in iter(self.credentials.keys()):
            #returning the value
            return self.credentials[key]
        else:
            #Prints error message if the key is not found.
            print("ERROR: Invalid credentials")
    
    """ set_credentials is a setter function that sets the email 
        and password of the user"""
    def set_credentials(self,key,value):
        #Assign the value to the key
        self.credentials[key]= value

    """ test_change_status is a testcase that chnages the status of 
        friends in a profile's friendList"""
    def test_change_friend_status(self):
        #Logging Messages
        print("LOG: Executing Post-on Wall Test")
        #Logging Messages
        print("LOG: Selecting Link Text 'Ben Mathew'")
        #Navigating to the User's Wall Page
        link_element = self.driver.find_element_by_link_text("Ben")
        #Logging Messages
        print("LOG: Link Text Element clicked")
        #Click on Link
        link_element.click()
    
    """ test_logout_test is module that logouts out of a user's facebook 
        profile"""
    def test_logout_test(self):
        #Select the anchor Button
        link_element = self.driver.find_element_by_id("pageLoginAnchor")
        #Clicks on the link
        link_element.click()
    
    """ test_login is a module that tests the facebook login feature"""
    def test_login(self):
        #Logging Messages
        print("LOG: Executing Facebook Log-in Test")
        #Setting input for Email by findind the input 
        #field by id
        email = self.driver.find_element_by_id("email")
        #Logging Messages
        print("LOG: Selecting Email textField")
        #Sets the emaill field to the revelant key.
        email.send_keys(self.get_credentials("email"))
        #Logging Message
        print("LOG: Setting password to text Field")
        
        #Setting input for password by selecting the 
        #password by id   
        pw = self.driver.find_element_by_id("pass")
        #Logging message 
        print("LOG: Setting Password Textfield")
        #Sets the input for the password field.
        pw.send_keys(self.get_credentials("pw"))
        #Logging Message
        print("LOG: Setting text for password field")
        #Logging Message
        print("LOG: Driver set to wait for 20 seconds")
        #Sets the selenium thread to sleep for 2 seconds
        time.sleep(2)    
        #Logging Message
        print("LOG: Selecting the Login Button") 
        #Selecting the login input by id
        login = self.driver.find_element_by_id('u_0_2')            
        print("LOG: Login Button Clicked")
        #Send submit key to the input.
        login.submit()
    
    """ test_setup is a module that sets up the necessary preconditions 
        for the test."""
    def test_setup(self):
        #Logging Messages
        print("LOG: Navigating to Facebook")
        #Navigate to facebook.com
        self.utils.goToUrl("https://www.facebook.com")
        #Logging Message
        print("LOG: Logging in as Ben Mathew")
        #sets the email key to value "dbm0204@gmail.com"
        self.set_credentials("email","dbm0204@gmail.com")
        #sets the pw key to the value "Anil4kunj!$"
        self.set_credentials("pw","Anil4kunj!$")
    
    """test_main is a module that executes the test"""
    def test_main(self):
        #Executes the Login List
        self.test_login()
        #Puts the webdriver to sleep for 10 seconds
        time.sleep(10)
        #Executes the change friendship status test.
        self.test_change_friend_status()
        #Puts the webdriver to sleep for 10 seconds.
        time.sleep(10)
    
    """ test_exit is a module that closes the session of 
        browser"""
    def test_exit(self):
        #Quits the current session of the browser.
        self.driver.quit()

    """test_clean perfroms the clean job after the test."""
    def test_clean(self):
        self.driver.close()
