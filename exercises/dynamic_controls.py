import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By # Helps get elements through selectors for interaction
from selenium.webdriver.support.ui import WebDriverWait # Helps uses expected conditions and explicit waits
from selenium.webdriver.support import expected_conditions as EC

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()
    
    def test_add_remove_checkbox(self):
        driver = self.driver
        remove_checkbox_btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/form[1]/button'
            )
        remove_checkbox_btn.click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'message')))
        
        if message.text == "It's gone!":
            add_checkbox_btn = remove_checkbox_btn
        
        add_checkbox_btn.click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'message')))
        
        if message.text == "It's back!":
            print('Button removed and added successfully!')
            checkbox = driver.find_element_by_id('checkbox')
            checkbox.click()
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_selected(checkbox))
        
    def test_enable_disable_input(self):
        driver = self.driver
        enable_input_btn = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/form[2]/button'
        )
        enable_input_btn.click()

        input_xpath = '/html/body/div[2]/div/div[1]/form[2]/input'

        input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, input_xpath)))

        if input.is_enabled:
            disable_input_btn = enable_input_btn
            input.send_keys("It's working!")
        
        disable_input_btn.click()
        
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'message')))
        
        if message.text == "It's disabled!":
            print('Button enabled and disabled successfully!')
 
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)