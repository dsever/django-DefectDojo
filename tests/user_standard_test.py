import unittest
import sys
from pathlib import Path
from base_test_class import BaseTestCase
from user_test import UserTest


class UserStandardTest(BaseTestCase):

    @staticmethod
    def add_user_read_only_parameter():
        f = open('/app/dojo/settings/local_settings.py', 'w')
        f.write("USER_PROFILE_READ_ONLY=True")
        f.close()

    @staticmethod
    def reload_service():
        Path("/app/dojo/settings/settings.py").touch()

    def login_standard_page(self):
        driver = self.driver
        driver.get(self.base_url + "login")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys('propersahm')
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys('Def3ctD0jo&')
        driver.find_element_by_css_selector("button.btn.btn-success").click()

        self.assertFalse(self.is_element_by_css_selector_present('.alert-danger', 'Please enter a correct username and password'))
        return driver

    def test_standard_user_login(self):
        self.login_standard_page()

    def test_admin_profile_form(self):
        self.driver.get(self.base_url + "profile")
        self.assertTrue(self.driver.find_element_by_id('id_first_name').is_enabled())

    def test_user_profile_form(self):
        self.driver.get(self.base_url + "profile")
        self.assertFalse(self.driver.find_element_by_id('id_first_name').is_enabled())


def suite():

    suite = unittest.TestSuite()
    # Add each test the the suite to be run
    # success and failure is output by the test
    suite.addTest(BaseTestCase('test_login'))
    suite.addTest(UserTest('test_create_user'))
    suite.addTest(UserStandardTest('test_admin_profile_form'))
    suite.addTest(BaseTestCase('test_logout'))
    suite.addTest(UserStandardTest('test_standard_user_login'))
    suite.addTest(UserStandardTest('test_user_profile_form'))
    suite.addTest(BaseTestCase('test_logout'))
    suite.addTest(BaseTestCase('test_login'))
    suite.addTest(UserTest('test_user_delete'))

    return suite


if __name__ == "__main__":
    UserStandardTest.add_user_read_only_parameter()
    UserStandardTest.reload_service()
    runner = unittest.TextTestRunner(descriptions=True, failfast=True, verbosity=2)
    ret = not runner.run(suite()).wasSuccessful()
    BaseTestCase.tearDownDriver()
    sys.exit(ret)
