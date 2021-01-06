#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 15:17
# @Author  : Chris.Ma
#测试用例发现，使用htmltestrunner去运行测试用例
import time
import unittest
import os
from util import config, htmlTestRunner


class TestRunner(object):
    def __init__(self):
        self.suite = unittest.TestLoader().discover("testSuite")
        cf = config.Config()
        self.report_folder = cf.get_value("run.conf", "report", "file_dir")

    def startrun(self, name, title):
        package_path = os.path.abspath("..")
        file_path = os.path.join(package_path, self.report_folder)
        os.chdir(file_path)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        file_name = title + now + ".html"
        fp = open(file_name, "wb")
        runner = htmlTestRunner.HTMLTestRunner(stream=fp, title=name, description=title)
        runner.run(self.suite)
        fp.close()


if __name__ == '__main__':
    # 执行用例
    tr = TestRunner()
    tr.startrun("测试套件", "自动化测试")