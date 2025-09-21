#import logging
#logger = logging.getLogger(__name__)
#logger.propagate = False
#logger.info('hello from SQLMonitorLogger')

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.info('hello from SQLMonitorLogger')