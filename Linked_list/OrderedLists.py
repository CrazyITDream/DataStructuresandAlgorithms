# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          OrderedLists
# Author:        xiaohuo
# Date:          2020/4/2
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   14:47 
# -------------------------------------------------------------------------------
from Linked_list.Node import Node

"""
python实现有序列表
"""


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        判断有序列表是否为空
        :return:
        """
        return self.head == None

    def length(self):
        """
         返回列表中元素的个数
        :return:返回一个整数
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def add(self, InsertData):
        """
        添加一个元素
        :return: 无
        """
        current = self.head
        previous = None  # 上一个节点
        stop = False
        while current != None and not stop:
            if current.getData() > InsertData:
                stop = not stop  # 实际返回应为True
            else:
                previous = current
                current = current.getNext()

        tmp = Node(InsertData)
        if previous == None:  # 有序列表中无元素
            tmp.setNext(self.head)  # 设置插入元素的下一个节点为空
            self.head = tmp  # 将插入元素作为头节点
        else:
            tmp.setNext(current)  # 插入元素的下一个节点
            previous.setNext(tmp)  # 设置下一个节点

    def Search(self, SearchData):
        """
        在列表中搜索 SearchData ，它接受一个元素作为参数，并且返回布尔值
        :return:布尔值
        """
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == SearchData:
                found = not found
            else:
                if current.getData() > SearchData:
                    stop = not stop
                else:
                    current = current.getNext()
        return found

    def remove(self, RemoveData):
        """
        从其中移除 RemoveData ，它接受一个元素作为参数，并且修改列表。
        :param RemoveData:
        :return:被移除的数
        """
        current = self.head
        previous = None
        while current != None:
            if current.getData() == RemoveData:
                return True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, IndexData):
        """
         假设IndexData已经在列表中，并返回该元素在列表中的位置。它接受一个元素作为参数，并且返回该元素的下标
        :param IndexData:查找下标的元素
        :return:元素的下标
        """
        current = self.head
        count = 0
        while current != None:
            if current.getData() == IndexData:
                return count
            else:
                count += 1
                current = current.getNext()

        return count

    def pop(self):
        """
        假设列表不为空，并移除列表中的最后一个元素。它不需要参数，且会返回一个元素
        :return:被删除的元素
        """
        current = self.head
        previous = None
        removeData = None
        while current != None:
            if current.getNext() == None:
                removeData = current.getData()
                previous.setNext(self.head)
                return removeData
            else:
                previous = current
                current = current.getNext()
        return removeData

    def pop(self, delIndex):
        """
        假设在指定位置delIndex存在元素，并移除该位置上的元素。它接受位置参数，且会返回一个元素
        :param delIndex:
        :return:
        """
        current = self.head
        previous = None
        count = 0
        removeData = None
        while current != None:
            if count == delIndex:
                removeData = current.getData()  # 获取要被删除的值
                previous.setNext(current.getNext())  # 将要被删除的值的上一个节点的下一个节点指向被删元素的下一个节点
                return removeData
            else:
                count += 1
                previous = current
                current = current.getNext()

        return removeData
