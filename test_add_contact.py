# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_create_contact(self):
        self.login()
        self.create_new_contact(
            Contact(firstname="Trolo", middlename="trololoev", lastname="Trolevich", nickname="Trol", title="God",
                    company="JSC", address="TroloLand", email="trolo@yandex.ru"))
        self.logout()

    def test_create_empty_contact(self):
        self.login()
        self.create_new_contact(
            Contact(firstname="", middlename="", lastname="", nickname="", title="",
                    company="", address="", email=""))
        self.logout()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def create_new_contact(self, Contact):
        self.driver.find_element_by_link_text("add new").click()
        self.driver.find_element_by_name("firstname").send_keys(Contact.firstname)
        self.driver.find_element_by_name("middlename").send_keys(Contact.middlename)
        self.driver.find_element_by_name("lastname").send_keys(Contact.lastname)
        self.driver.find_element_by_name("nickname").send_keys(Contact.nickname)
        self.driver.find_element_by_name("title").send_keys(Contact.title)
        self.driver.find_element_by_name("company").send_keys(Contact.company)
        self.driver.find_element_by_name("address").send_keys(Contact.address)
        self.driver.find_element_by_name("email").send_keys(Contact.email)
        self.driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.driver.find_element_by_link_text("home page").click()

    def login(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.driver.quit()
