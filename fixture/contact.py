import re

from model.Contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_in_form(contact)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_in_form(self, contact):
        driver = self.app.driver
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.homephone)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobilephone)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.workphone)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_homepage()
        driver.find_elements_by_name("selected[]")[index].click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def open_homepage(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("addressbook/") and len(driver.find_elements_by_name("Delete")) > 0):
            driver.find_element_by_link_text("home").click()

    def update_contact_by_index(self, contact, index):
        driver = self.app.driver
        self.open_homepage()
        driver.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        self.fill_in_form(contact)
        driver.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def update_first_contact(self):
        self.update_contact_by_index(0)

    def return_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def count(self):
        driver = self.app.driver
        self.open_homepage()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_homepage()
            self.contact_cache = []
            for element in (driver.find_elements_by_css_selector("tr")[1:]):
                contact_id = element.find_element_by_name("selected[]").get_attribute('value')
                cells = element.find_elements_by_tag_name('td')
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(
                    Contact(lastname=last_name, firstname=first_name, id=contact_id, homephone=all_phones[0],
                            mobilephone=all_phones[1], workphone=all_phones[2]))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.open_homepage()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_homepage()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone)
