from model.Contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_in_form(contact, driver)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage(driver)
        self.contact_cache = None

    def fill_in_form(self, contact, driver):
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


    def delete(self):
        driver = self.app.driver
        self.open_homepage(driver)
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
        self.contact_cache = None

    def open_homepage(self, driver):
        if not (driver.current_url.endswith("addressbook/") and len(driver.find_elements_by_name("Delete")) > 0):
            driver.find_element_by_link_text("home").click()

    def update(self, contact):
        driver = self.app.driver
        self.open_homepage(driver)
        driver.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_in_form(contact, driver)
        driver.find_element_by_name("update").click()
        self.return_to_homepage(driver)
        self.contact_cache = None

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home page").click()

    def count(self):
        driver = self.app.driver
        self.open_homepage(driver)
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_homepage(driver)
            self.contact_cache = []
            for element in (driver.find_elements_by_css_selector("tr")[1:]):
                contact_id = element.find_element_by_name("selected[]").get_attribute('value')
                cells = element.find_elements_by_tag_name('td')
                last_name = cells[1].text
                first_name = cells[2].text
                self.contact_cache.append(Contact(lastname=last_name, firstname=first_name, id=contact_id))
        return list(self.contact_cache)
