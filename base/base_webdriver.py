from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWebDriver:

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            print(f'Locator type {locator_type} is not valid/supported...')
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print('Element found')
        except:
            print('Element not found')
        return element

    def click_element(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print(f'Clicked on element with locator: {locator}, locatorType: {locator_type}')
        except:
            print(f'Cannot click on element with locator: {locator}, locatorType: {locator_type}')

    def type_keys(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print(f'Sent data on element with locator: {locator}, locatorType: {locator_type}')
        except:
            print(f'Cannot send data on element with locator: {locator}, locatorType: {locator_type}')

    def is_element_present(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print('Element Found')
                return True
            else:
                print('Element not found')
                return False
        except:
            print('Element not found')
            return False

    def wait_for_element(self, locator, locator_type='id'):
        by_type = self.get_by_type(locator_type)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by_type, locator)))






