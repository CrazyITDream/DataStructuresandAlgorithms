# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          dequebase
# Author:        xiaohuo
# Date:          2020/3/30
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   22:53 
# -------------------------------------------------------------------------------
"""
用 Python 实现双端队列。（假设前端在列表的右端）
"""


class Deque:
    def __init__(self):
        self.deque_list = []

    def isEmpty(self):
        """
        判断双端队列是否为空
        :return: 为空放回false,不为空返回true
        """
        return self.deque_list == []

    def addFront(self, deque):
        """
        将一个元素添加到双端队列的前端
        :param deque:添加的元素
        :return:None
        """
        self.deque_list.append(deque)

    def addRear(self, deque):
        """
        将一个元素添加到双端队列的后端
        :param deque:添加的元素
        :return:None
        """
        self.deque_list.insert(0, deque)

    def removeFront(self):
        """
        从双端队列的前端移除一个元素
        :return:被移除的元素
        """
        return self.deque_list.pop()

    def removeRear(self):
        """
        从双端队列的后端移除一个元素
        :return:被移除的元素
        """
        return self.deque_list.pop(0)

    def size(self):
        """
         返回双端队列中元素的数目
        :return:元素的数目
        """
        return len(self.deque_list)













