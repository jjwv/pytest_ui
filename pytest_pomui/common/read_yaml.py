#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2019-12-13 14:46
# Software: PyCharm

import yaml
import os

def readyml(yamlPath):
    '''
    读取yaml文件内容
    realPath: 文件的真是路径，绝对路径地址
    '''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确 %s" %yamlPath)
    #open方法直接打开读出来
    f = open(yamlPath, "r", encoding="utf-8")
    cfg =f.read()
    # print(cfg)
    d = yaml.load(cfg)  #用load方法转字典
    print("读取的测试文件数据： %s" %d)
    return d
if __name__ == '__main__':
    readyml('/Users/cuiwenhao/Documents/cekai/pytest_pomui/case/articleclassify.yml')