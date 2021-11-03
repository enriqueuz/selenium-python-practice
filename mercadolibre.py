import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('https://mercadolibre.com/')
        driver.maximize_window()
    
    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        # location.click()
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        # condition.click()
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_class_name(
            'andes-dropdown__trigger'
            )
        order_menu.click()
        higher_price = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]/div[2]/div[2]/div'
            )
        higher_price.click()
        sleep(3)

        articles = []
        
        for i in range(5):
            try:
                article_name = driver.find_element_by_xpath(
                    f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2'
                    ).text 
                article_price = driver.find_element_by_xpath(
                    f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]'
                    ).text
            except NoSuchElementException:
                article_name = driver.find_element_by_xpath(
                    f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/a/h2'
                    ).text
                article_price = driver.find_element_by_xpath(
                    f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[3]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]'
                    ).text
            
            article = {'name': article_name, 'price': article_price}
            articles.append(article)
        print(articles)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)