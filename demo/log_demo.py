import logging
import logging.config



logging.basicConfig(level=logging.DEBUG,
                format='[%(levelname)s] %(asctime)s %(filename)s %(lineno)d %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='run.log',
                filemode='a')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')


logging.config.fileConfig("logger.conf")
logger = logging.getLogger("root")
logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')