from base.base_webdriver import BaseWebDriver


class LoginPage(BaseWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'
    _user_icon = '.gravatar'

    def click_login_link(self):
        login_link_present = self.wait_for_element(locator=self._login_link, locator_type='link')
        if login_link_present:
            self.click_element(locator=self._login_link, locator_type='link')

    def enter_email(self, email):
        email_field_present = self.wait_for_element(locator=self._email_field)
        if email_field_present:
            self.type_keys(email, self._email_field)

    def enter_password(self, password):
        password_field_present = self.wait_for_element(locator=self._password_field)
        if password_field_present:
            self.type_keys(password, self._password_field)

    def click_login_button(self):
        self.click_element(self._login_button, locator_type='name')

    def login(self, email, password):

        self.click_login_link()

        self.enter_email(email)
        self.enter_password(password)

        self.click_login_button()
        self.driver.implicitly_wait(3)

    def user_is_logged_in(self):
        user_icon_present = self.is_element_present(locator=self._user_icon, locator_type='css')
        return user_icon_present
