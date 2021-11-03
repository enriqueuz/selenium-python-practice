import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Test fixture to prepare everything. """
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        """ Test fixture with the output. """
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reports', 
            report_name='hello-world-report')
        )