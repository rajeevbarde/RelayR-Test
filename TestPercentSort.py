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

    # Test to verify if the decending order of 24 hour percent is working as expected
    def test_24Percent_descending(self):

        # Click on the percentage column
        percent_column = self.driver.find_element_by_id("th-change")
        percent_column.click()

        # Collect all the values
        percent_values = self.driver.find_elements_by_class_name("percent-24h")
        largest_percent = float(self.driver.find_element_by_class_name("percent-24h").get_attribute("data-usd"))
        issue_found = False;

        # Logic to verify percentage are shown in descending order
        for item in percent_values:
            current_percent = float(item.get_attribute("data-usd"))

            if largest_percent >= current_percent:
                largest_percent = current_percent
                continue
            else:
                issue_found = True
                break

        assert issue_found is not True

if __name__ == '__main__':
    unittest.main()

