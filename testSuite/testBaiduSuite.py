#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 14:47
# @Author  : Chris.Ma
#测试用例组织，业务层操作与测试数据继续组织
import unittest
from testScript.baiduScript import baiduScript
from util.config import Config
from util.excelReader import CreateExcel
from time import sleep
import ddt

from util.webdriverApi import WebDriver

filezpath = "testdata.xlsx"
at = CreateExcel(filezpath)
head = ["search1","search2","expected"]
op = at.datacel(head)

@ddt.ddt
class TestSuite(unittest.TestCase):
    #初始化driver
    driver = WebDriver()

    @classmethod
    def setUpClass(cls):
        cls.Script = baiduScript(cls.driver)
        cls.config = Config()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #测试输入框
    @ddt.data(*op)
    def test_case_01(self,op):
        self.Script.open_baidu(self.config.get_value("url.conf","url","baidu_url"))
        self.Script.search(op["search1"] + ' ' + op["search2"])
        sleep(2)
        print(op["expected"])
        #页面源码获取的有点问题
        page = self.Script.get_page()
        assert op["expected"] in page

    #测试link
    def test_case_02(self):
        self.Script.open_baidu(self.config.get_value("url.conf","url","baidu_url"))
        self.Script.test_link()
        sleep(2)
        assert "魏大勋" not in self.Script.get_page()