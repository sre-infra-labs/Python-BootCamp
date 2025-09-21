import logging

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')