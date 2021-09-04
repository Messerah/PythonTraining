class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        driver.find_element_by_link_text("group page").click()

    def update(self, group):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("group page").click()
