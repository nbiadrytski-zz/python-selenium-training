from base.base_webdriver import BaseWebDriver
from pages.main.main_page import MainPage
from utils.custom_config import CustomConfigParser


class LoginPage(BaseWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cfg = CustomConfigParser(config_path='configfiles/locators.ini', section='login_page')
        self._email_field = self.cfg.get_locator('email_field')
        self._password_field = self.cfg.get_locator('password_field')
        self._login_button = self.cfg.get_locator('login_button')
        self._user_icon = self.cfg.get_locator('user_icon')
        self._error_text = self.cfg.get_locator('error_text')

    def enter_email(self, email):
        self.type_keys(email, self._email_field)

    def enter_password(self, password):
        self.type_keys(password, self._password_field)

    def click_login_button(self):
        self.click_element(self._login_button, 'name')

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return MainPage(self.driver)

    def user_is_logged_in(self):
        if self.is_element_present(self._user_icon, 'css'):
            self.logger.info(f'User successfully logged in.')
            return True
        else:
            self.logger.error(f'User did not log in.')
            return False
