from utils.logger import Logger


class Error(Exception, Logger):
    def __init__(self, message):
        Logger.__init__(self.logger)
        self.message = message

    def __str__(self):
        return f'{self.message}'


class ElementNotFoundError(Error):
    def __init__(self, locator, locator_type, timeout):
        self.message = f'\nWaited {timeout} seconds for element with locator: ' \
                       f'"{locator}", locator_type: "{locator_type}", ' \
                       f'but DID NOT FIND it... \nIt is either does not exist or not visible yet.'
        self.logger.error(self.message)


class LocatorTypeNotFoundError(Error):

    def __init__(self, locator_type, locators):
        self.supported_locators = LocatorTypeNotFoundError.get_supported_locators(locators)
        self.message = f'{locator_type} locator is not supported... ' \
                       f'\nThe following locators are supported: {self.supported_locators}'
        self.logger.error(self.message)

    @staticmethod
    def get_supported_locators(locators):
        locators_list = []
        for locator, _ in locators.items():
            locators_list.append(locator)
        return locators_list
