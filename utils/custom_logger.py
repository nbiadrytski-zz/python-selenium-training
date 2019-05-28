import logging


class CustomLogger:

    @property
    def logger(self):
        return logging.getLogger(__name__)
