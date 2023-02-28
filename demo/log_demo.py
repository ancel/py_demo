import logging
import logging.config
import log_demo_sub
import traceback

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
LOGGER.error('This is error message')
try:
    raise ValueError('A error happend !')
except ValueError as e:
    LOGGER.error("error 1")
    print('----')
    LOGGER.error(str(e))
    print('----')
    LOGGER.error("error 2", exc_info=True)
    print('----')
    LOGGER.exception('error 3')
    print('----')
    # 打印详细日志 方法1
    traceback.print_exc()
    print('----')
    # 打印详细日志 方法2
    e_detail = traceback.format_exc()
    print(e_detail)

log_demo_sub.say()