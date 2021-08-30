from selenium import webdriver

from fixture.Group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def create_new_contact(self, contact):
        self.driver.find_element_by_link_text("add new").click()
        self.driver.find_element_by_name("firstname").send_keys(contact.firstname)
        self.driver.find_element_by_name("middlename").send_keys(contact.middlename)
        self.driver.find_element_by_name("lastname").send_keys(contact.lastname)
        self.driver.find_element_by_name("nickname").send_keys(contact.nickname)
        self.driver.find_element_by_name("title").send_keys(contact.title)
        self.driver.find_element_by_name("company").send_keys(contact.company)
        self.driver.find_element_by_name("address").send_keys(contact.address)
        self.driver.find_element_by_name("email").send_keys(contact.email)
        self.driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.driver.find_element_by_link_text("home page").click()

    def destroy(self):
        self.driver.quit()
