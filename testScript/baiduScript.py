#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 14:20
# @Author  : Chris.Ma
from pageAction.baiduAction import baiduAction


class baiduScript():
    def __init__(self,web_driver):
        self.Action = baiduAction(web_driver)

    #打开百度页面
    def open_baidu(self,url):
        self.Action.open_baidu(url)

    #搜索
    def search(self,searchKey):
        self.Action.type_search(searchKey)
        self.Action.click_baidu()

    #测试link
    def test_link(self):
        self.Action.click_hao123()
        self.Action.back()
        self.Action.click_news()

    #获取页面源码
    def get_page(self):
        return self.Action.get_page()