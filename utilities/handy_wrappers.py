from selenium.webdriver.common.by import By


class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("Locator type is not supported")
        return False

    def find_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_locator_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

