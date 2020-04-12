# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          orderSearch
# Author:        xiaohuo
# Date:          2020/4/5
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:39 
# -------------------------------------------------------------------------------
"""
python实现有序列表搜索
"""


# def orderSearch(searchList, searchValue):
#     """
#     实现有序列表搜索
#     :param searchList:有序列表
#     :param searchValue:搜索的值
#     :return:没有搜索到返回False，搜索成功返回True
#     """
#     for listIndex in range(len(searchList)):
#         if searchValue in searchList:
#             return True
#         else:
#             if searchValue < searchList[listIndex]:
#                 return False
#             else:
#                 return False

def orderSearch(searchList, searchValue):
    """
    实现有序列表搜索
    :param searchList:有序列表
    :param searchValue:搜索的值
    :return:没有搜索到返回False，搜索成功返回True
    """
    count = 0
    found = False
    while count > len(searchList) and not found:
        if  searchList[count] == searchValue:
            return not found
        else:
            if searchList[count] > searchValue:
                return found
            else:
                count += 1
    return found


print(orderSearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 5))








