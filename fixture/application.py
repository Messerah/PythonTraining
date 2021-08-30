from selenium import webdriver


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def create_new_contact(self, Contact):
        self.driver.find_element_by_link_text("add new").click()
        self.driver.find_element_by_name("firstname").send_keys(Contact.firstname)
        self.driver.find_element_by_name("middlename").send_keys(Contact.middlename)
        self.driver.find_element_by_name("lastname").send_keys(Contact.lastname)
        self.driver.find_element_by_name("nickname").send_keys(Contact.nickname)
        self.driver.find_element_by_name("title").send_keys(Contact.title)
        self.driver.find_element_by_name("company").send_keys(Contact.company)
        self.driver.find_element_by_name("address").send_keys(Contact.address)
        self.driver.find_element_by_name("email").send_keys(Contact.email)
        self.driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.driver.find_element_by_link_text("home page").click()

    def login(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def create_new_group(self, Group):
        self.driver.find_element_by_link_text("groups").click()
        self.driver.find_element_by_name("new").click()
        self.driver.find_element_by_name("group_name").send_keys(Group.name)
        self.driver.find_element_by_name("group_header").send_keys(Group.header)
        self.driver.find_element_by_name("group_footer").send_keys(Group.footer)
        self.driver.find_element_by_name("submit").click()
        self.driver.find_element_by_link_text("group page").click()

    def destroy(self):
        self.driver.quit()
