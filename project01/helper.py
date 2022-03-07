import logging

logger = logging.getLogger(__name__) # name of the module
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)
logger.propagate = False
logger.info('hello from logger')

# logging.debug('This is a debug message')
# logging.info('This is a info message')
# logging.warning('This is a warning message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')

