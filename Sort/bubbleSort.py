# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          bubbleSort
# Author:        xiaohuo
# Date:          2020/4/7
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   23:35 
# -------------------------------------------------------------------------------
"""
python实现冒泡算法
时间复杂度O(n^2)
"""


# def bubbleSort(alist):
#     """
#     冒泡排序
#     :param alist: 排序列表
#     :return: 排序后的列表
#     """
#     for i in range(len(alist)-1, 0, -1):
#         for j in range(i):
#             if alist[j] > alist[j+1]:
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#     return alist


# def shortBubbleSort(alist):
#     """
#     短冒泡排序
#     :param alist: 排序列表
#     :return: 排序后的列表
#     """
#     exchange = True
#     for i in range(len(alist)-1, 0, -1):
#         exchange = False
#         for j in range(i):
#             if alist[j] > alist[j+1]:
#                 exchange = True
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#     return alist


def shortBubbleSort(alist):
    """
    短冒泡排序
    :param alist: 排序列表
    :return: 排序后的列表
    """
    exchange = True
    alistLen = len(alist)-1
    while alistLen > 0 and exchange:
        exchange = False
        for i in range(alistLen):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        alistLen -= 1
    return alist


print(shortBubbleSort([1, 5, 3, 9, 2]))










