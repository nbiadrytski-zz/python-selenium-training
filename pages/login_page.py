from pages.main_page import MainPage
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, locators_config_section='login_page')
        self.login_page_driver = driver

        self._email_field = self.locators_cfg.get_locator('email_field')
        self._password_field = self.locators_cfg.get_locator('password_field')
        self._login_button = self.locators_cfg.get_locator('login_button')
        self._user_icon = self.locators_cfg.get_locator('user_icon')
        self._error_text = self.locators_cfg.get_locator('error_text')

    def enter_email(self, email):
        self._driver.type_keys(email, self._email_field)

    def enter_password(self, password):
        self._driver.type_keys(password, self._password_field)

    def click_login_button(self):
        self._driver.click_element(self._login_button, 'name')

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return MainPage(self.login_page_driver)

    def user_is_logged_in(self):
        if self._driver.is_element_present(self._user_icon, 'css'):
            self.logger.info(f'User logged in.')
            return True
        else:
            self.logger.info(f'User did not log in.')
            return False
