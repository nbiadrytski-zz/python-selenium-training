from selenium.webdriver.common.by import By
from utils.errors import LocatorTypeNotFoundError


class LocatorType:

    locators = {
        'id':    By.ID,
        'name':  By.NAME,
        'xpath': By.XPATH,
        'css':   By.CSS_SELECTOR,
        'class': By.CLASS_NAME,
        'link':  By.LINK_TEXT,
    }

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type in self.locators:
            locator_type = self.locators[locator_type]
        else:
            raise LocatorTypeNotFoundError(locator_type, self.locators)
        return locator_type
