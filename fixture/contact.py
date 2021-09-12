class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_in_form(contact, driver)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage(driver)

    def fill_in_form(self, contact, driver):
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("email").send_keys(contact.email)

    def delete(self):
        driver = self.app.driver
        self.open_homepage(driver)
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()

    def open_homepage(self, driver):
        driver.find_element_by_link_text("home").click()

    def update(self, contact):
        driver = self.app.driver
        self.open_homepage(driver)
        driver.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_in_form(contact, driver)
        driver.find_element_by_name("update").click()
        self.return_to_homepage(driver)

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home page").click()

    def count(self):
        driver = self.app.driver
        self.open_homepage(driver)
        return len(driver.find_elements_by_name("selected[]"))

