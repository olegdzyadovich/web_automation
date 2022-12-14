from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from utilities.logger import *
import logging as log


class BaseObject:
    log = log_method(logLevel=log.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def __selenium_by(self, by):
        selectors_dict = {'css': By.CSS_SELECTOR,
                          'xpath': By.XPATH,
                          'id': By.ID,
                          'class': By.CLASS_NAME,
                          'link_text': By.LINK_TEXT,
                          'tag_name': By.TAG_NAME,
                          'name': By.NAME,
                          'partial_link': By.PARTIAL_LINK_TEXT}

        return selectors_dict[by]

    def is_visible(self, by, locator):
        self.log.info(f"{locator} is visible")
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(by), locator)))


    def is_present(self, by, locator):
        return self.wait.until(ec.presence_of_element_located((self.__selenium_by(by), locator)))

    def is_clickable(self, by, locator):
        return self.wait.until(ec.element_to_be_clickable((self.__selenium_by(by), locator)))


    def is_typing(self,by, locator, data):
        self.is_visible(by,locator).send_keys(data)

    def is_clicking(self, by, locator):
        self.is_clickable(by, locator).click()

    def is_equal(self, expected, actual):
        assert expected==actual, "error"

    def is_text(self, by, locator):
        element_text = self.is_visible(by, locator).text
        return element_text



