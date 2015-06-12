# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from groupproperties import Groups

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class AddGroupHomework(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_homepage(self, wd):
        wd.get("http://localhost:8000/addressbook/group.php")

    def login(self, wd, username, pwd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_Group(self, wd, Groups):
        # create group
        wd.find_element_by_name("new").click()
        # filling group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Groups.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Groups.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Groups.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_AddGroupHomework(self) :
        success = True
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", pwd="secret")
        self.create_Group(wd, Groups(name="Homeworkgroup", header="TestHeader", footer="TestFooter"))
        self.logout(wd)
        self.assertTrue(success)

    def test_AddGroupHomeworkEmptyValues(self) :
        success = True
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", pwd="secret")
        self.create_Group(wd, Groups(name="", header="", footer=""))
        self.logout(wd)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
