#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris
import xlrd
import os
from util.logger import Logger

logger = Logger(logger="ExcelReader").getlog()


class CreateExcel:
    filename = ""
    def __init__(self,filename):
        self.filename = filename

    def datacel(self, head):
        all_case = []
        head_len = len(head)
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/data/' + self.filename
        file = xlrd.open_workbook(file_path)
        me = file.sheets()[0]
        nrows = me.nrows
        for i in range(1, nrows):
            dict = {}
            index = 0
            for l in head:
                dict[l] =  str(me.cell(i, index).value)
                index += 1
            all_case.append(dict)
        return all_case


if __name__ == "__main__":
    filezpath = "testdata.xlsx"
    at = CreateExcel(filezpath)
    head = ["search1","search2","except"]
    op = at.datacel(head)
    print(op)