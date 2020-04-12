# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          exercise
# Author:        xiaohuo
# Date:          2020/4/4
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   19:08 
# -------------------------------------------------------------------------------


# def calculateFactorial(n):
#     """
#     递归函数来计算数的阶乘
#     :param n:
#     :return:
#     """
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * calculateFactorial(n - 1)
#
#
# print(calculateFactorial(3))


# def reversalList(reList):
#     """
#     反转列表
#     :param reList:列表
#     :return:
#     """
#     if len(reList) == 0:
#         return reList
#     else:
#         return reversalList(reList[len(reList)-1:])
#
#
# print(reversalList([1, 2, 3, 4, 5, 6]))


"""
python实现背包问题
"""
def calculateMaxValue(wight, value, lenWight, maxWight):
    if lenWight < 0 or maxWight < 0:
        return 0
    res = calculateMaxValue(wight, value, lenWight-1, maxWight)
    if maxWight >= wight[lenWight]:
        res = max(res, value[lenWight] + calculateMaxValue(wight, value, lenWight-1,maxWight-wight[lenWight]))
        return res


wight = [2, 3, 4, 5, 9]
value = [3, 4, 8, 8, 10]
print(calculateMaxValue(wight, value, len(wight), 20))



































