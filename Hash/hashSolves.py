# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          hashSolve
# Author:        xiaohuo
# Date:          2020/4/6
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   22:53 
# -------------------------------------------------------------------------------

"""
python实现解决散表的冲突问题
"""


# def hashSolve(hashList, hashValue):
#     """
#     python实现线性探测
#     :param hashList: 整数集合
#     :param hashValue:散列表大小
#     :return:整数集合
#     """
#     hashLists = [None for i in range(hashValue)]
#     hashLists2 = []
#     for i in hashList:
#         hashIndex = i % hashValue
#         if hashLists[hashIndex] == None:
#             hashLists[hashIndex] = i
#         else:
#             """
#             检测下一个是否为空，为空则插入，不为空则继续判断下一个，如果都不为空，从列表开始重新判断，并插入
#             """
#             found = False
#             while not found:
#                 hashIndex = hashIndex + 1
#                 if hashIndex >= len(hashLists):
#                     for j in range(len(hashLists)):
#                         if hashLists[j] == None:
#                             hashLists[j] = i
#                             break
#                     found = True
#                 else:
#                     if hashLists[hashIndex] == None:
#                         hashLists[hashIndex] = i
#                         found = True
#                         break
#
#     return hashLists

# def hashSolve(hashList, hashValue):
#     """
#     python实现再散列
#     :param hashList: 整数集合
#     :param hashValue:散列表大小
#     :return:整数集合
#     """
#     hashLists = [None for i in range(hashValue)]
#     for i in hashList:
#         hashIndex = i % hashValue
#         if hashLists[hashIndex] == None:
#             hashLists[hashIndex] = i
#         else:
#             """
#             检测下一个是否为空，为空则插入，不为空则继续判断下一个，如果都不为空，从列表开始重新判断，并插入
#             """
#             found = False
#             while not found:
#                 hashIndex += 3
#                 if hashIndex >= len(hashLists):
#                     for j in range(0, len(hashLists)):
#                         if hashLists[j] == None:
#                             hashLists[j] = i
#                             break
#                     found = True
#                 else:
#                     if hashLists[hashIndex] == None:
#                         hashLists[hashIndex] = i
#                         break
#
#     return hashLists


# print(hashSolve([54, 26, 93, 17, 77, 31, 44, 55, 20], 11))
