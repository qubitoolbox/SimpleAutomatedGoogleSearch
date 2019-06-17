#impor libraries
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import time	
"""
A very simple test case that can search for anything
in Google. The baseline can be improved to search for
anything in an automated way. Objects or arrays can be
be created if multiple search are wanted to test. 

Note that this was indented with spaces. In case python
complaints of unwanted TABS
"""
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #specify path to where the chromedriver is installed
        self.driver = webdriver.Chrome(	
			executable_path='path to chrome driver')

    def test_search_in_python_org(self):
        try:
            #set a value to end program if needed
            runprog = True
            while runprog:
                #invoke the driver to begin test
            driver = self.driver
            #Retrieve the site, in this case Google (can be any)
            driver.get("https://www.google.com")
            self.assertIn("Google", driver.title)
            time.sleep(1)
            #current search box element
            elem = driver.find_element_by_name('q')
            #search input inside strings
            elem.send_keys("Just some random automated search")
            elem.send_keys(Keys.RETURN)
            time.sleep(8)
        except ValueError:
            print("Seems like elements got woozed.")
if __name__ == "__main__":
    unittest.main()
