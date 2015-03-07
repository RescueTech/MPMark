from selenium import webdriver
import unittest


class ItemCRUDTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_an_item_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        # user opens the site to find their supermarket's
        # name in the page title.
        self.assertIn('MPMark V01', self.browser.title)
        # he also sees a link to add new products
        # and another link to see all existing products.
        # he addes a new product
        # he goes back to see the products he added
        # and sees a list with one item in it

if __name__ == '__main__':
    unittest.main(warnings='ignore')
