from base.locator_types import LocatorType
from utils.custom_logger import CustomLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.errors import ElementNotFoundError


class BaseWebDriver(CustomLogger):

    def __init__(self, driver):
        CustomLogger.__init__(self.logger)
        self.driver = driver
        self.loc_type = LocatorType()

    def get_element(self, locator, locator_type='id', timeout=10):
        by_type = self.loc_type.get_by_type(locator_type)
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by_type, locator)))
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
