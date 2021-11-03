import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(('dress', 5), ('music', 5)) # Elements to be searched with expected results count
    @unpack # Let's you unpack the tuples above and consult them individually
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        # Find elements generates a list
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)
        
        self.assertEqual(expected_count, len(products))


        

            


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
