class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_group_list(driver)
        driver.find_element_by_name("new").click()
        self.fill_in_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_group_page(driver)

    def fill_in_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).send_keys(text)

    def return_to_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_list(driver)
        self.select_first_group(driver)
        driver.find_element_by_name("delete").click()
        self.return_to_group_page(driver)

    def select_first_group(self, driver):
        driver.find_element_by_name("selected[]").click()

    def update_first_group(self, group):
        driver = self.app.driver
        self.open_group_list(driver)
        self.select_first_group(driver)
        driver.find_element_by_name("edit").click()
        self.fill_in_form(group)
        driver.find_element_by_name("update").click()
        self.return_to_group_page(driver)

    def open_group_list(self, driver):
        driver.find_element_by_link_text("groups").click()
