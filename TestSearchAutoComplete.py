import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class RelayrTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        self.driver.get("https://coinmarketcap.com/")

    def tearDown(self):
        self.driver.quit()

    # Test to verify search's autocomplete feature is working
    def test_search_autocomplete(self):

        # Enter 'Stellar' on the searchbox
        search_box = self.driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/form/div/span/input")
        search_box.send_keys("Stellar")

        # Auto-complete dropdown should contain 'Stellar (XLM)'
        search_box.send_keys(Keys.ARROW_DOWN)
        search_webelement = self.driver.find_element_by_class_name("tt-suggestion")
        search_result = search_webelement.find_elements_by_tag_name("p")
        search_result_text = search_result[0].text

        assert search_result_text is not ""

if __name__ == '__main__':
    unittest.main()

