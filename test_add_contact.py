# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("TEST")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("TEST")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("TEST")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("TEST")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("TEST")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("TEST")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("TEST")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("Test")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("TEST")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
