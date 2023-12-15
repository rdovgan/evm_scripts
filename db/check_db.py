from db_connection import read_setting
from logger import log


log_name = 'check.log'


log(log_name, read_setting('test_setting'))
