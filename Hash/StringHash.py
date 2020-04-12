# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          StringHash
# Author:        xiaohuo
# Date:          2020/4/6
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   20:05 
# -------------------------------------------------------------------------------

"""
python实现对字符串构建简单的散列函数
"""


def spliceHashStr(String, tablesize):
    """
    没有添加权重计算散列值
    :param String:字符串
    :param tablesize:散列表的长度
    :return:散列值
    """
    sum = 0
    for i in range(len(String)):
        sum += ord(String[i])
    return sum % tablesize      # 4


def hashStr(String, tablesize):
    """
    添加权重计算散列值
    :param String:字符串
    :param tablesize:散列表的长度
    :return:散列值
    """
    sum = 0
    for i in range(len(String)):
        sum = sum + (ord(String[i])*(i+1))      # 为字符添加权重，为下标加1
    return sum % tablesize          # 3


print(spliceHashStr('cat', 11))









