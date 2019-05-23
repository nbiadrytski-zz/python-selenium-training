from selenium import webdriver
from pages.home.login_page import LoginPage


class TestLogin:

    def test_valid_login(self):
        base_url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        login_page = LoginPage(driver)
        login_page.login('test@email.com', 'abcabc')

        assert login_page.user_is_logged_in()
