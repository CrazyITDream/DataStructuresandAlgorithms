# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ListSum
# Author:        xiaohuo
# Date:          2020/4/3
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   14:35 
# -------------------------------------------------------------------------------

"""
实现对列表求和
"""


# 没有使用递归方法
# def listSum(numList):
#     """
#     对数字列表求和
#     :param numList: 求和的列表
#     :return: 列表的和
#     """
#     theListSum = 0
#     for i in numList:
#         theListSum += i
#     return theListSum
#
#
def listSum(SumList):
    """
    递归求和函数
    :param SumList: 求和列表
    :return:求和之后的值
    """
    if len(SumList) == 1:
        return SumList[0]
    else:
        return SumList[0] + listSum(SumList[1:])

print(listSum([i for i in range(1,20,2)]))
























































