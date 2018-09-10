import logging

# 根据模块名获取日志
# LOGGER = logging.getLogger(__name__)
#主模块设置logger之后，子模块可以直接获取到logger
LOGGER = logging.getLogger()
def say():
    print('sdg')
    LOGGER.info('sub')    
    print(__name__)
    