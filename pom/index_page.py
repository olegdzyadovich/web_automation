from base.base_object import BaseObject
from locators.locators import LocatorsIndexPage as l, LocatorsMainPage as l2




class IndexPage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_username(self):
        self.is_typing('xpath',l.USERNAME_FIELD_XPATH, 'standard_user')

    def input_password(self):
        self.is_typing('css', l.PASSWORD_FIELD_CSS, 'secret_sauce')

    def press_login_btn(self):
        self.is_clicking('xpath', l.BUTTON_XPATH)

    def assertion_products(self):
        expected_result = "PRODUCTS"
        actual_results = self.is_visible("xpath" , l2.SUB_TITLE_XPATH)
        self.is_equal(expected_result,actual_results)

