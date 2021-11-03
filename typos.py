import unittest
from selenium import webdriver


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_dynamic_controls(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector(
            '#content > div > p:nth-child(3)'
        )
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        self.assertIsNotNone(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        # while text_check != correct_text:
        #     paragraph_to_check = driver.find_element_by_css_selector(
        #     '#content > div > p:nth-child(3)'
        #     )
        #     text_check = paragraph_to_check.text
        #     driver.refresh()

        # while not found:
        #     if text_check == correct_text:
        #         tries += 1
        #         driver.refresh()
        #         found = True
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector(
                "#content > div > p:nth-child(3)"
                )
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1
        
        found = True
        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
