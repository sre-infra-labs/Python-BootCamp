import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')

import SqlmonitorLogger

SqlmonitorLogger.info('This is a info message')
