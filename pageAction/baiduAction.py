#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 13:51
# @Author  : Chris.Ma
from util.iniHelper import IniHelper
from time import sleep

#百度页面元素的原子操作
from util.webdriverApi import WebDriver


class baiduAction():
    #构造函数
    def __init__(self, web_driver):
        self.driver = web_driver
        self.source = IniHelper()

    #打开百度页面
    def open_baidu(self, url):
        self.driver.open(url)

    #在百度输入框中输入内容
    def type_search(self, searchKey):
        self.driver.type(self.source.get_value("baiduPage.ini","TextInput","百度输入框") ,searchKey)

    #点击百度
    def click_baidu(self):
        self.driver.click(self.source.get_value("baiduPage.ini","Button","百度一下"))

    #点击hao123
    def click_hao123(self):
        self.driver.click(self.source.get_value("baiduPage.ini","Link","hao123"))

    #点击新闻
    def click_news(self):
        self.driver.click(self.source.get_value("baiduPage.ini","Link","新闻"))

    #获取页面资源
    def get_page(self):
        return self.driver.get_page_source()

    #返回上一个页面
    def back(self):
        self.driver.back()


if __name__ =="__main__":
    WD = WebDriver()
    BD = baiduAction(WD)
    BD.open_baidu("http://www.baidu.com")
    sleep(2)
    print(BD.get_page())
    WD.quit()


