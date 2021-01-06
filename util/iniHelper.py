#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris

import configparser
import os


class IniHelper(object):
    def __init__(self):
        self.source_folder = "PageObject"

    '''
        读取INI文件
        :param file_name:配置文件名称
    '''

    def get_source_file(self, file_name):
        try:
            config = configparser.ConfigParser()
            file_path = self.get_file_path(self.source_folder, file_name)
            config.read(file_path, encoding="utf-8-sig")
            return config
        except Exception as e:
            print("read config file error:" + str(e))


    '''
        读取文件所在路径，默认读取Config文件夹的文件，如需修改，实例化类时，传文件夹名称
        注意：只能读取com.note包及子包下的文件
        :param file_name:文件名称
    '''
    @staticmethod
    def get_file_path(folder_name, file_name):
        source_path = os.path.abspath("..")
        file_path = os.path.join(source_path, folder_name)
        file_path = os.path.join(file_path, file_name)
        return file_path

    '''
        读取配置文件
        :param file_name:配置文件名称
        :param section:配置文件中的section
        :param key:配置文件中的key
    '''
    def get_value(self, file_name, section, key):
        try:
            config = self.get_source_file(file_name)
            value = config.get(section, key)
            return value
        except Exception as e:
            print("get value failed:" + str(e))


if __name__ == '__main__':
    ini = IniHelper()
    # print(sys.argv[0])
    print (ini.get_value("baiduPage.ini", "Link", "新闻"))
