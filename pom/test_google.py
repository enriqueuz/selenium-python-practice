import unittest
from selenium import webdriver
from google_page import GooglePage

#@classmethod
class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
