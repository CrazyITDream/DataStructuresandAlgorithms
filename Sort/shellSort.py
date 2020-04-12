# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          shellSort
# Author:        xiaohuo
# Date:          2020/4/10
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   22:33 
# -------------------------------------------------------------------------------

"""
python实现希尔排序
时间复杂度O(n^2),随着增量,增量为(2^k)-1时间复杂度为O(n^(3/2))
"""


def shellSort(sortList):
    subLen = len(sortList) // 2
    while subLen > 0:
        for startPosition in range(subLen):
            gapInsertionSort(sortList, startPosition, subLen)
        subLen = subLen // 2
    return sortList


def gapInsertionSort(sortList, start, subLen):
    for i in range(start + subLen, len(sortList), subLen):
        currentvalue = sortList[i]
        position = i

        while position >= subLen and sortList[position - subLen] > currentvalue:
            sortList[position] = sortList[position - subLen]
            position = position - subLen
        sortList[position] = currentvalue


print(shellSort([1, 8, 9, 31, 54, 2, 76, 99]))







