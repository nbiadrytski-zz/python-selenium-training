import pytest
from base.driver_factory import WebDriverFactory


BASE_URL = 'https://letskodeit.teachable.com/'


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', help='Browser to run tests against')


@pytest.fixture()
def get_driver(request):
    browser = request.config.getoption('--browser')

    factory = WebDriverFactory(browser)
    driver = factory.get_driver_instance()

    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)

    return driver


@pytest.fixture()
def welcome_page(get_driver):
    from pages.welcome.welcome_page import WelcomePage
    wp = WelcomePage(get_driver)
    wp.navigate(BASE_URL)
    return wp


@pytest.fixture()
def log_in(welcome_page):
    def login_(email, password):
        login_page = welcome_page.click_login_link()
        main_page = login_page.login(email, password)
        return main_page
    return login_
