#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
__author__ = 'zhanghaiyan'

"""获取项目某路径下某文件绝对路径"""
import os
def get_Path():
    path=os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__=='__main__':
    print('路径为：',get_Path())