class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self):
        driver = self.app.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return (driver.find_elements_by_xpath("//div[@id='top']/form/b")).text == "("+username+")"

    def ensure_login(self):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in():
                return
            else:
                self.logout()
        self.login()
