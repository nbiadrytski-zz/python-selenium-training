import configparser


class CustomConfigParser:
    def __init__(self, config_path, section):
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)
        self.section = section

    def get_locator(self, locator):
        return self.parser.get(self.section, locator)
