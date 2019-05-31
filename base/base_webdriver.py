from base.locator_types import LocatorType
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.errors import ElementNotFoundError


class BaseWebDriver(Logger):

    def __init__(self, driver):
        self._driver = driver
        self._locators = LocatorType()

    def go_to_page(self, url):
        self._driver.get(url)

    def get_element(self, locator, locator_type='id', timeout=10):
        by_type = self._locators.get_by_type(locator_type)
        element = None
        try:
            element = WebDriverWait(self._driver, timeout).until(ec.visibility_of_element_located((by_type, locator)))
            self.logger.debug(
                f'\nElement with locator: "{locator}", locator_type: "{locator_type}" is ready for work.')
        except (NoSuchElementException, TimeoutException):
            ElementNotFoundError(locator, locator_type, timeout)
        return element

    def click_element(self, locator, locator_type='id'):
        self.get_element(locator, locator_type).click()

    def type_keys(self, data, locator, locator_type='id'):
        self.get_element(locator, locator_type).send_keys(data)

    def is_element_present(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        if element is not None:
            return True
        else:
            return False
