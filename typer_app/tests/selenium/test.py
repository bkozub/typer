import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import selenium

class SeleniumTestTypes(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)

    @staticmethod
    def _test_login(self,driver):
        driver.get("http://localhost:8081")
        self.assertIn('Typer', driver.title)
        driver.find_element_by_id("id_username").click()
        driver.implicitly_wait(50000)
        #driver.find_element_by_id("id_username").clear()
        driver.implicitly_wait(50000)
        driver.find_element_by_id("id_username").send_keys("automat23")
        driver.implicitly_wait(50000)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("SeleniumTest")
        driver.implicitly_wait(50000)
        driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        driver.implicitly_wait(50000)
        hello_element = driver.find_element_by_css_selector('div.jumbotron>h1')
        self.assertEqual(hello_element.text,"Hello")

    @staticmethod
    def _test_logout(self,driver):
        driver.find_element_by_css_selector('li.dropdown').click()
        driver.implicitly_wait(50000)
        driver.find_element_by_css_selector('li.dropdown>ul>li:last-child>a').click()
        self.assertIn('login',driver.current_url)

    def test_user_type(self):
        driver = self.driver
        self._test_login(self,driver)
        driver.implicitly_wait(50000)
        driver.find_element_by_css_selector('a[href="/type/"]').click()
        driver.find_element_by_id("id_comp_id").click()
        driver.implicitly_wait(50000)
        Select(driver.find_element_by_id("id_comp_id")).select_by_visible_text("Karpacz 2017-01-04")
        driver.implicitly_wait(50000)
        driver.find_element_by_id("id_jumpers").click()
        driver.implicitly_wait(50000)
        Select(driver.find_element_by_id("id_jumpers")).select_by_visible_text("Stefan Kraft")
        driver.implicitly_wait(50000)
        driver.find_element_by_id("id_jumpers").click()
        driver.implicitly_wait(50000)
        driver.find_element_by_css_selector('button[type="submit"]').click()
        driver.implicitly_wait(50000)
        allert = driver.find_element_by_css_selector('div.alert')
        self.assertEqual(allert.text,'×\nYou type a jumper!')
        driver.find_element_by_css_selector('li.dropdown').click()
        driver.implicitly_wait(50000)
        driver.find_element_by_css_selector('li.dropdown>ul>li[id="user_types"]>a').click()
        driver.implicitly_wait(50000)
        type = driver.find_element_by_css_selector('ul[id="typed_jumpers"]>li:last-child')
        self.assertIn("Stefan Kraft",type.text)
        self._test_logout(self,driver)

if __name__ == "__main__":
    unittest.main()
