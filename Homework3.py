# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import  unittest
from AddGroupHomework import AddGroupHomework
from groupproperties import Formfields

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Homework3(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def OpenHomepage(self, wd):
        wd.get("http://localhost:8000/addressbook/")



    def AddPerson(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fillingForm(self, wd, Formfields):
        # filling the fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Formfields.firstName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Formfields.lastName)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Formfields.companyName)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Formfields.email)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Formfields.mobile)

    def confirm(self, wd):
        # confirm enetering
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def test_Homework3(self):
        success = True
        wd = self.wd
        self.OpenHomepage(wd)
        AddGroupHomework.login(self, wd, username="admin", pwd="secret")
        self.AddPerson(wd)
        self.fillingForm(wd, Formfields("pavel", "Ageyev", "3Shape", "pavel.ageyev@3shape.com", "+380672351002"))
        self.confirm(wd)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
