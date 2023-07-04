import logging
import os

from dotenv import load_dotenv


class LoggerService:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.file_handler = None

    def __enter__(self):
        self.file_handler = logging.FileHandler(self.log_file)
        self.file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)
        return self.logger

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()

    def info(self, message):
        self.logger.info(message)

    def close(self):
        self.file_handler.close()


load_dotenv()


def log(log_name, message):
    with LoggerService(f'{os.getenv("LOGS_DIRECTORY")}/{log_name}') as logger:
        logger.info(message)