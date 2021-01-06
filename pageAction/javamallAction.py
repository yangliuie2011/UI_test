#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 16:36
# @Author  : Chris.Ma
from util.iniHelper import IniHelper


class javamallAction():
    # 构造函数
    def __init__(self, web_driver):
        self.driver = web_driver
        self.source = IniHelper()

    # 打开javamall页面(打开页面，删除cookie，填入cookie)
    def open_javamall(self, url):
        self.driver.open(url)
    # 删除cookie
    def delete_cookie(self):
        self.driver.clear_cookie()

    # 填入cookie
    def add_cookie(self,name, value):
        self.driver.add_cookie(name,value)

    # 悬停设置
    def move_to_settings(self):
        self.driver.move_to_element(self.source.get_value("javamallPage.ini","Button","设置"))

    # 点击管理员管理
    def click_admin(self):
        self.driver.click(self.source.get_value("javamallPage.ini", "Button", "管理员管理"))