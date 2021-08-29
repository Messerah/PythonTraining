# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver


#from Contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.create_new_contact(driver)
        self.return_to_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def create_new_contact(self, driver):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys("TEST")
        driver.find_element_by_name("middlename").send_keys("TEST")
        driver.find_element_by_name("lastname").send_keys("TEST")
        driver.find_element_by_name("nickname").send_keys("TEST")
        driver.find_element_by_name("title").send_keys("TEST")
        driver.find_element_by_name("company").send_keys("TEST")
        driver.find_element_by_name("address").send_keys("TEST")
        driver.find_element_by_name("email").send_keys("Test")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, driver):
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.driver.quit()
