import logging
import os
from logging import config

def log_config():
    #'读取日志配置文件'
    path = 'resources/loguser.conf'
    if os.path.exists(path):
        with open(path,"r",encoding = 'utf-8') as f:
            logging.config.fileConfig(f)
    #创建一个日志器logger
    logger = logging.getLogger(name="fileLogger")
    rotating_logger = logging.getLogger(name="rotatingFileLogger")

    logger.debug('debug')
    logger.info('info')
    logger.warning('warn')
    logger.error('error')
    logger.critical('critical')

    rotating_logger.debug('debug')
    rotating_logger.info('info')
    rotating_logger.warning('warn')
    rotating_logger.error('error')
    rotating_logger.critical('critical')