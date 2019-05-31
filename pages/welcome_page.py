from pages.login_page import LoginPage
from pages.base_page import BasePage


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, locators_config_section='welcome_page')
        self.welcome_page_driver = driver

        self._login_link = self.locators_cfg.get_locator('login_link')

    def navigate(self, url):
        self._driver.go_to_page(url)
        self.logger.info(f'Navigated to {url}')

    def click_login_link(self):
        self._driver.click_element(self._login_link, 'link')
        return LoginPage(self.welcome_page_driver)
