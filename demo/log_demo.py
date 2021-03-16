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

# 若要是所有模块都是用现有的日志配置，则需要在模块加载前加载配置文件，或者在加载配置文件的时候设定disable_existing_loggers=False
logging.config.fileConfig("logger.conf", disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
# LOGGER = logging.getLogger('root') 
#主模块设置logger之后，子模块可以直接用如下方法获取到logger，而不需要进行任何设置
# LOGGER = logging.getLogger()

LOGGER.debug('This is debug message')
LOGGER.info('This is info message')
LOGGER.warning('This is warning message')
try:
    raise Exception()
except Exception as e:
    LOGGER.error('This is error message', exc_info=True)
    LOGGER.exception('This is exception message')

log_demo_sub.say()