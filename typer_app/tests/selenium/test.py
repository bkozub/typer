import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SeleniumTestTypes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @staticmethod
    def _test_login(self,driver):
        driver.get("http://127.0.0.1:8000")
        self.assertIn('Typer', driver.title)
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("automat23")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("SeleniumTest")
        driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        driver.implicitly_wait(30)
        hello_element = driver.find_element_by_css_selector('div.jumbotron>h1')
        self.assertEqual(hello_element.text,"Hello")

    @staticmethod
    def _test_logout(self,driver):
        driver.find_element_by_css_selector('li.dropdown').click()
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector('li.dropdown>ul>li:last-child>a').click()
        self.assertIn('login',driver.current_url)

    def test_user_type(self):
        driver = self.driver
        self._test_login(self,driver)
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector('a[href="/type/"]').click()
        driver.find_element_by_id("id_comp_id").click()
        driver.implicitly_wait(30)
        Select(driver.find_element_by_id("id_comp_id")).select_by_visible_text("Karpacz 2017-01-04")
        driver.implicitly_wait(2000)
        driver.find_element_by_id("id_jumpers").click()
        driver.implicitly_wait(30)
        Select(driver.find_element_by_id("id_jumpers")).select_by_visible_text("Stefan Kraft")
        driver.implicitly_wait(2000)
        driver.find_element_by_id("id_jumpers").click()
        driver.find_element_by_css_selector('button[type="submit"]').click()
        allert = driver.find_element_by_css_selector('div.alert')
        self.assertEqual(allert.text,'×\nYou type a jumper!')
        driver.find_element_by_css_selector('li.dropdown').click()
        driver.find_element_by_css_selector('li.dropdown>ul>li[id="user_types"]>a').click()
        type = driver.find_element_by_css_selector('ul[id="typed_jumpers"]>li:last-child')
        self.assertIn("Stefan Kraft",type.text)
        self._test_logout(self,driver)



if __name__ == "__main__":
    unittest.main()




