import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from unittest.suite import TestSuite

class RightUserTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.hudl.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//a[@href="'+"/login"+'"]').click()
        print("Clicked on Log in button and loaded log in page")

    def testCorrectUser(self):
        #user credentials
        username = "afilipem@gmail.com"
        password = "y4KDvEfW5%s7"
        self.driver.find_element(By.ID,"email").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        print("User information field sent")
        self.driver.find_element(By.ID,"logIn").click()
        print("User page loaded")
        time.sleep(10)
        titleOfWebPage = self.driver.title
        print(titleOfWebPage)
        self.assertEqual("Home - Hudl", titleOfWebPage, "webpage title is not matching")

    def tearDown(self):
        #close the browser window
        self.driver.quit()

class WrongUserTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.hudl.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//a[@href="'+"/login"+'"]').click()
        print("Clicked on Log in button and loaded log in page")

    def testCorrectUser(self):
        #user credentials
        username = "bfilipem@gmail.com"
        password = "y4KDvEfW5%s7"
        self.driver.find_element(By.ID,"email").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        print("User information field sent")
        self.driver.find_element(By.ID,"logIn").click()
        print("User page loaded")
        time.sleep(10)
        titleOfWebPage = self.driver.title
        print(titleOfWebPage)
        self.assertEqual("Log In - Hudl", titleOfWebPage, "webpage title is not matching")

    def tearDown(self):
        #close the browser window
        self.driver.quit()

if __name__ == '__main__':

    #create the suite from the test classes
    print("Starting the test suite")
    suite = TestSuite()
    #load the tests
    tests = unittest.TestLoader()

	#add the tests to the suite
    suite.addTests(tests.loadTestsFromTestCase(RightUserTestCase))
    suite.addTests(tests.loadTestsFromTestCase(WrongUserTestCase))
    print("No. of test cases present : ", suite.countTestCases())

    #run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print("Finished!")