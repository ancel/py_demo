import logging
import logging.config

import log_demo_sub



# logging.basicConfig(level=logging.DEBUG,
#                 format='[%(levelname)s] %(asctime)s %(filename)s %(lineno)d %(message)s',
#                 datefmt='%Y-%m-%d %H:%M:%S',
#                 filename='run.log',
#                 filemode='a')
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')


logging.config.fileConfig("logger.conf")
# LOGGER = logging.getLogger("root")
LOGGER = logging.getLogger(__name__)
#主模块设置logger之后，子模块可以直接用如下方法获取到logger，而不需要进行任何设置
# LOGGER = logging.getLogger()

LOGGER.debug('This is debug message')
LOGGER.info('This is info message')
LOGGER.warning('This is warning message')
LOGGER.error('This is error message')

log_demo_sub.say()