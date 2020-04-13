# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          mergeSort
# Author:        xiaohuo
# Date:          2020/4/11
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:06 
# -------------------------------------------------------------------------------
"""
python实现归并排序
    注：列表的长度为 n 时，能切分log2n 次
"""


def mergeSort(sortList):
    if len(sortList) > 1:
        subLen = len(sortList) // 2
        lefthalf = sortList[:subLen]
        righthalf = sortList[subLen:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while len(lefthalf) > i and len(righthalf) > j:
            if lefthalf[i] < righthalf[j]:
                sortList[k] = lefthalf[i]
                i += 1
            else:
                sortList[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            sortList[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            sortList[k] = righthalf[j]
            j += 1
            k += 1
    return sortList


print(mergeSort([45, 65, 2, 52, 98, 16, 22]))
