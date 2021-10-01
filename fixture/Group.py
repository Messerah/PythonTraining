from model.Group import Group


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
        self.group_cache = None

    def fill_in_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def return_to_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_list(driver)
        self.select_first_group(driver)
        driver.find_element_by_name("delete").click()
        self.return_to_group_page(driver)
        self.group_cache = None

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
        self.group_cache = None

    def open_group_list(self, driver):
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def count(self):
        driver = self.app.driver
        self.open_group_list(driver)
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_list(driver)
            self.group_cache = []
            for element in (driver.find_elements_by_css_selector("span.group")):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
