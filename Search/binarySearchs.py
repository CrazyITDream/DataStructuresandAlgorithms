# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          binarySearch
# Author:        xiaohuo
# Date:          2020/4/5
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:54 
# -------------------------------------------------------------------------------
"""
python实现有序列表二分搜索
"""


# def binarySearch(searchList, searchValue):
#     """
#     有序列表二分搜索
#     :param searchList: 有序列表
#     :param searchValue: 搜索值
#     :return: 存在列表中返回True,不存在返回False
#     """
#     if len(searchList) == 0:
#         return False
#     else:
#         if searchList[len(searchList) // 2] == searchValue:
#             return True
#         else:
#             if searchList[len(searchList) // 2] > searchValue:
#                 return binarySearch(searchList[:len(searchList) // 2], searchValue)
#             else:
#                 return binarySearch(searchList[len(searchList) // 2 + 1:], searchValue)
#
#
# print(binarySearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 12], 6))
