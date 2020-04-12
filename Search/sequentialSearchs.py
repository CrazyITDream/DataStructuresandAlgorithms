# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          sequentialSearch
# Author:        xiaohuo
# Date:          2020/4/5
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:24 
# -------------------------------------------------------------------------------

"""
python实现无序列表搜索
"""


# def sequenceSearch(searchList ,searchNum):
#     for i in range(len(searchList)):
#        return True if searchList[i] == searchNum else False

def sequenceSearch(searchList, searchNum):
    count = 0
    found = False

    while count < len(searchList) and not found:
        if searchList[count] == searchNum:
            return not found
        else:
            count += 1
    return found


print(sequenceSearch([1, 2, 3, 4, 5, 7, 8, 22], 22))
