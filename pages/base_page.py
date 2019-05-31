from base.base_webdriver import BaseWebDriver
from utils.config_parser import ConfigParser
from utils.logger import Logger


class BasePage(Logger):
    def __init__(self, driver, locators_config_section):
        self._driver = BaseWebDriver(driver)
        self.locators_cfg = ConfigParser(config_path='configfiles/locators.ini',
                                         locators_config_section=locators_config_section)
