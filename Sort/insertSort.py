# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          insertSort
# Author:        xiaohuo
# Date:          2020/4/9
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   23:31 
# -------------------------------------------------------------------------------
"""
python实现插入排序
时间复杂度为O(n^2)
"""


# def insertSort(sortList):
#     """
#     插入排序
#     :param sortList:排序的列表
#     :return:排序后的列表
#     """
#     newSortList = []
#     for i in range(0, len(sortList)):
#         if i == 0:
#             newSortList.append(min(sortList))
#         else:
#             for j in range(len(newSortList)):
#                 if sortList[i] > newSortList[j]:
#                     newSortList.insert(j, sortList[i])
#                     break
#     newSortList.reverse()
#     return newSortList

def insertSort(sortList):
    """
    插入排序
    :param sortList: 排序的列表
    :return: 排序后的列表
    """
    for index in range(1, len(sortList)):

        currentValue = sortList[index]
        position = index

        while position > 0 and sortList[position-1] > currentValue:
            sortList[position] = sortList[position-1]
            position -= 1
        sortList[position] = currentValue

    return sortList


print(insertSort([9, 34, 56, 22, 12, 17, 7, 4]))