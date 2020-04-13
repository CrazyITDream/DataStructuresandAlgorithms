# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          quickSort
# Author:        xiaohuo
# Date:          2020/4/13
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   22:34 
# -------------------------------------------------------------------------------

"""
python实现快速排序
"""


def quickSort(sortList):
    quickSortHelper(sortList, 0, len(sortList)-1)


def quickSortHelper(sortList, first, last):
    if first < last:
        splitpoint = partition(sortList, first, last)

        quickSortHelper(sortList, first, splitpoint-1)
        quickSortHelper(sortList, splitpoint+1, last)


def partition(sortList, first, last):
    pivotvalue = sortList[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and sortList[leftmark] <= pivotvalue:
            leftmark += 1

        while sortList[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            sortList[leftmark], sortList[rightmark] = sortList[rightmark], sortList[leftmark]

    sortList[first], sortList[rightmark] = sortList[rightmark], sortList[first]

    return rightmark








