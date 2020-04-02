# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          Node
# Author:        xiaohuo
# Date:          2020/3/31
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   10:47 
# -------------------------------------------------------------------------------
"""
Node类的创建
"""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        """
        获取下一个值
        :return:
        """
        return self.data

    def getNext(self):
        """
        获取下一个节点
        :return:
        """
        return self.next

    def setData(self, NewData):
        """
        设置值下一个值
        :param NewData:
        :return:
        """
        self.data = NewData

    def setNext(self, NewNext):
        """
        下一个节点
        :param NewNext:
        :return:
        """
        self.next = NewNext
