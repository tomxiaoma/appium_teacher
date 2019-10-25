import logging.config
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
print(log_file_path)
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()
