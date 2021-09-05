class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_group_list(driver)
        driver.find_element_by_name("new").click()
        self.fill_in_form(driver, group)
        driver.find_element_by_name("submit").click()
        self.return_to_group_page(driver)

    def fill_in_form(self, driver, group):
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def return_to_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_list(driver)
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_group_page(driver)

    def update(self, group):
        driver = self.app.driver
        self.open_group_list(driver)
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.fill_in_form(driver, group)
        driver.find_element_by_name("update").click()
        self.return_to_group_page(driver)

    def open_group_list(self, driver):
        driver.find_element_by_link_text("groups").click()
