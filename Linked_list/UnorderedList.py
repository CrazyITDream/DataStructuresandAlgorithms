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

    def remove(self, RemoveNum):
        """
        删除某一个元素
        :return:
        """
        current = self.head  # 本节点
        previous = None  # 上一个节点
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

    def append(self, data):
        """
        增加一个数据至链表尾部
        :return:
        """
        tmp = Node(data)
        current = self.head
        while current != None:
            if current.getNext() == None:
                current.setNext(tmp)
                tmp.setNext(self.head)


    def index(self, Data):
        """
        返回指定元素的下标
        :param Data:指定元素
        :return: 找到返回元素的下标，没有找到返回None
        """
        current = self.head
        count = 0  # 记录下标
        while current != None:
            if current.getData() == Data:
                return count
            else:
                count += 1
                current = current.getNext()
        return None  # 没有找到改元素的下标

    def insert(self, index, Data):
        """
        根据index将数据插入到链表中
        :param index: 插入数据的下标
        :param Data: 插入的数据
        :return: None
        """
        tmp = Node(Data)
        current = self.head
        count = 0
        while current != None:
            if count == index:
                current.setNext(tmp)
                tmp.setNext(current.getNext())
            else:
                count += 1
                current = current.getNext()

    def pop(self):
        """
        不给出元素的下标删除元素，删除链表最开始那个
        :return:
        """
        current = self.head
        previous = None  # 上一个节点
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
        假设元素存在根据位置删除指定位置的元素，不存在返回False不存在
        :param pop: 传入的位置参数
        :return: 有返回被删除的元素，无返回False
        """
        current = self.head
        count = 0
        previous = None
        removeData = None
        while current != None:
            if delIndex == count:
                removeData = current.getData()
                previous.set(current.getNext())
                return removeData
            else:
                previous = current
                current = current.getNext()
        return removeData
















