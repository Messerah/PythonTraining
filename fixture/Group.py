class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Group):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(Group.name)
        driver.find_element_by_name("group_header").send_keys(Group.header)
        driver.find_element_by_name("group_footer").send_keys(Group.footer)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()
