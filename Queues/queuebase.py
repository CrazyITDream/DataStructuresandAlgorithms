# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          queue
# Author:        xiaohuo
# Date:          2020/3/30
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   10:00 
# -------------------------------------------------------------------------------

"""
python使用列表模拟队列,假设列表的头部就是队列的尾部
"""


class Queue:
    def __init__(self):
        self.queue = []         # 创建空列表，模拟初始为空的队列

    def enqueue(self, queue):
        """
        添加元素至队列的尾部
        :param queue:
        :return:
        """
        self.queue.insert(0, queue)

    def dequeue(self):
        """
        从队列中移除一个元素，没有返回值
        :return:被移除的元素
        """
        return self.queue.pop()

    def isEmpty(self):
        """
        检查队列是否为空，为空返回false,不为空返回true
        :return: 布尔值（false、true）
        """
        return self.queue == []

    def size(self):
        """
        返回队列中元素的数目
        :return: 队列中元素的数目
        """
        return len(self.queue)


"""
python使用列表模拟队列,假设列表的尾部就是队列的尾部
"""

# class Queues:
#     def __init__(self):
#         self.queue = []   # 创建空列表，模拟初始为空的队列
#
#     def enqueue(self, queue):
#         """
#         模拟添加元素至队列的尾部
#         :param queue:添加至队列的元素
#         :return:None
#         """
#         self.queue.append(queue)
#
#     def dequeue(self):
#         """
#         模拟队列删除头部元素
#         :return: 被删除的元素
#         """
#         return self.queue.pop(0)
#
#     def isEmpty(self):
#         """
#         判断队列是否为空
#         :return: 布尔值（false, true）
#         """
#         return self.queue == []
#
#     def size(self):
#         """
#         队列中元素的个数
#         :return: 元素的个数
#         """
#         return len(self.queue)


# if __name__ == '__main__':
#     q = Queue()
#     print(q.isEmpty())
#     q.enqueue(4)
#     q.enqueue('dog')
#     print(q.isEmpty())
#     print(q.queue)
#     print(q.dequeue())
#     print(q.size())









