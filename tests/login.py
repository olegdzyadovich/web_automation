from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.chrome.options import Options
from locators.locators import Locators as l

options = Options()


usernames = ("standard_user", "problem_user")
link = "https://www.saucedemo.com/"


class TestFirst:
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get(link)

    @pytest.mark.parametrize('users', usernames)
    def test_successful_login(self, users):
        username_field = self.browser.find_element(l.USERNAME_FIELD_XPATH)
        username_field.send_keys(users)
        time.sleep(2)
        password_field = self.browser.find_element(l.PASSWORD_FIELD_CSS)
        password_field.send_keys('secret_sauce')

        button = self.browser.find_element(l.BUTTON_XPATH)
        button.click()
        time.sleep(2)
        expected_text = 'PRODUCTS'
        actual_text = self.browser.find_element(By.CLASS_NAME, 'title').text

        assert actual_text == expected_text, f'Failed. Expected text is {expected_text}, but got {actual_text}'

    def test_unsuccessful_login(self):
        username_field = self.browser.find_element(l.USERNAME_FIELD_XPATH)
        username_field.send_keys('standard_user')
        time.sleep(2)
        password_field = self.browser.find_element(l.PASSWORD_FIELD_CSS)
        password_field.send_keys('invalid')

        button = self.browser.find_element(l.BUTTON_XPATH)
        button.click()
        time.sleep(2)
        expected_text = "Epic sadface: Username and password do not match any user in this service"
        actual_text = self.browser.find_element(By.XPATH, "//h3[@data-test='error']").text

        assert actual_text == expected_text, f'Failed. Expected text is {expected_text}, but got {actual_text}'

    def test_no_password_login(self):
        username_field = self.browser.find_element(l.USERNAME_FIELD_XPATH)
        username_field.send_keys('problem_user')
        time.sleep(2)
        button = self.browser.find_element(l.BUTTON_XPATH)
        button.click()
        expected = "Epic sadface: Password is required"
        actual = self.browser.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert expected == actual

    def test_locked_user(self):
        username_field = self.browser.find_element(l.USERNAME_FIELD_XPATH)
        username_field.send_keys('locked_out_user')
        time.sleep(2)
        password_field = self.browser.find_element(l.PASSWORD_FIELD_CSS)
        password_field.send_keys('secret_sauce')
        button = self.browser.find_element(l.BUTTON_XPATH)
        button.click()
        expected = "Epic sadface: Sorry, this user has been locked out."
        actual = self.browser.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert expected == actual

    def teardown_method(self):
        self.browser.quit()