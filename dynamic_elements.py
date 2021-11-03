import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()
    
    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(
                        f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a'
                        )
                    options.append(option_name.text)
                    print(options)
                except:
                    print("Option number {i} is not FOUND")
                    tries += 1
                    driver.refresh()
        
        print(f'Finished in {tries} tries')
 
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)