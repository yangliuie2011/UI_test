#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 16:46
# @Author  : Chris.Ma
import unittest

from testScript.javamallScript import javamallScript
from util.config import Config
from util.webdriverApi import WebDriver


class TestSuite(unittest.TestCase):
    #初始化driver
    driver = WebDriver()

    @classmethod
    def setUpClass(cls):
        cls.Script = javamallScript(cls.driver)
        cls.config = Config()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #测试输入框
    def test_case_01(self,op):
        self.Script.open_javamall("配置文件读取url","配置文件读取cookie name","配置文件读取cookie value")
        self.Script.click_admin()