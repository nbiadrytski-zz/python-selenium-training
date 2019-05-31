import configparser


class ConfigParser:
    def __init__(self, config_path, locators_config_section):
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)
        self.locators_config_section = locators_config_section

    def get_locator(self, locator):
        return self.parser.get(self.locators_config_section, locator)
