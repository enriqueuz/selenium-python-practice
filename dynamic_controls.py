import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By # Helps get elements through selectors for interaction
from selenium.webdriver.support.ui import WebDriverWait # Helps uses expected conditions and explicit waits
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()
    
    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element_by_css_selector(
            '#checkbox > input[type=checkbox]'
            )
        checkbox.click()

        # Css selectors instead of xpath makes code cleaner and clearer
        remove_add_button = driver.find_element_by_css_selector(
            '#checkbox-example > button'
            )
        remove_add_button.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#checkbox-example > button')
                )
            )
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector(
            '#input-example > button'
            )
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#input-example > button')
                )
            )
        
        text_area = driver.find_element_by_css_selector(
            '#input-example > input[type=text]'
            )
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)