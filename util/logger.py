#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris

import os.path
from util.config import Config
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        #读取配置文件中的日志设置
        cf = Config()
        self.log_dir = cf.get_value("log.conf", "basiclog", "log_dir")
        self.format = cf.get_value("log.conf", "basiclog", "format")

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        package_path = os.path.abspath("..")
        file_path = os.path.join(package_path, self.log_dir)
        file_name = cur_date + ".log"
        log_file = os.path.join(file_path, file_name)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(self.format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


