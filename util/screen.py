#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris.Ma
from util.webdriverApi import WebDriver
import os

class Screen(object):
    u'''这个应该截图功能的装饰器'''
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_file("Failed")
                raise
        return inner


if __name__ == '__main__':
    # 执行用例
    print(os.getcwd())