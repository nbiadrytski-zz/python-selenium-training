from base.base_webdriver import BaseWebDriver
from pages.login.login_page import LoginPage


class WelcomePage(BaseWebDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = 'Login'

    def navigate(self, url):
        self.driver.get(url)
        self.logger.info(f'Navigated to {url}')

    def click_login_link(self):
        self.click_element(self._login_link, 'link')
        return LoginPage(self.driver)
