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
"""


def mergeSort(sortList):
    subLen = len(sortList) // 2
    if len(sortList) > 0 and subLen > 0:
        rightList = sortList[:subLen]
        leftList = sortList[subLen:]
        return mergeSort(rightList)


mergeSort([45, 65, 2, 52, 98, 16, 22])









