import logging

#主模块设置logger之后，子模块可以直接获取到logger
logger = logging.getLogger()
def say():
    logger.info('sub')    