import logging


class Logger:

    @property
    def logger(self):
        return logging.getLogger(__name__)
