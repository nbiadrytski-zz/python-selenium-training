from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_driver_instance(self):
        driver = None

        if self.browser == 'ff':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()

        driver.maximize_window()
        return driver
