# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          UnorderedList
# Author:        xiaohuo
# Date:          2020/4/1
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   15:21 
# -------------------------------------------------------------------------------
"""
python实现无序列表（ unordered list ）
"""
from Linked_list.Node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        判断无序列表是否为空
        :return: false不为空，true为空
        """
        return self.head == None

    def add(self, item):
        """
        添加数据到无序链表中
        :param item: 添加的值
        :return:
        """
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def length(self):
        """
        计算链表长度
        :return: 链表长度
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, Nodenum):
        """
        查找元素是否在无序链表中
        :param Nodenum: 查找的元素
        :return:
        """
        current = self.head
        while current != None:
            if Nodenum == current.getData():
                return True
            else:
                current = current.getNext()
        return False

    def remove(self,RemoveNum):
        """
        删除某一个元素
        :return:
        """
        current = self.head     # 本节点
        previous = None         # 上一个节点
        while current != None:
            if RemoveNum == current.getData():
                return True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())




