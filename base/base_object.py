from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class BaseObject:
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
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(by), locator)))

    def is_present(self, by, locator):
        return self.wait.until(ec.presence_of_element_located((self.__selenium_by(by), locator)))

    def is_clickable(self, by, locator):
        return self.wait.until(ec.element_to_be_clickable((self.__selenium_by(by), locator)))


