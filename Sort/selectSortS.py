# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          selectSort
# Author:        xiaohuo
# Date:          2020/4/9
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   22:44 
# -------------------------------------------------------------------------------
"""
python实现选择排序
时间复杂度为O(n^2)
"""


def selectSoert(sortList):
    for i in range(len(sortList)-1, 0, -1):
        maxIndex = 0
        for j in range(1, i+1):
            if sortList[j] > sortList[maxIndex]:
                maxIndex = j
        sortList[i], sortList[maxIndex] = sortList[maxIndex], sortList[i]
    return sortList


print(selectSoert([1, 5, 3, 9, 2]))








