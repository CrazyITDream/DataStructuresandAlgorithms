# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          palchecker
# Author:        xiaohuo
# Date:          2020/3/30
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   23:12 
# -------------------------------------------------------------------------------
"""
python实现回文检测器
"""
from Deques.dequebase import Deque


def palcheckers(String):
    """
    实现回文检测
    :param String:需要检测的回文串
    :return:False 和 True
    """
    chardeque = Deque()

    for str in String:
        if str != " ":
            chardeque.addRear(str)

    while chardeque.size() > 1:
        first = chardeque.removeFront()
        list = chardeque.removeRear()
        if first != list:
            return False
    return True


if __name__ == '__main__':
    print(palcheckers('l istatsil'))










