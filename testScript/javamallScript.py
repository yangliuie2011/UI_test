#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 16:42
# @Author  : Chris.Ma
from pageAction.javamallAction import javamallAction


class javamallScript():
    def __init__(self,web_driver):
        self.Action = javamallAction(web_driver)

    #打开javamall页面并登录
    def open_javamall(self,url,name,value):
        self.Action.open_javamall(url)
        self.Action.delete_cookie()
        self.Action.add_cookie(name,value)
        self.Action.open_javamall(url)

    #悬停设置，点击管理员管理
    def click_admin(self):
        self.Action.move_to_settings()
        self.Action.click_admin()