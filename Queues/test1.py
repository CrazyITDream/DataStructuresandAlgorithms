# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          test1
# Author:        xiaohuo
# Date:          2020/3/30
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   10:54 
# -------------------------------------------------------------------------------
"""
使用队列模拟：传土豆
"""
from Queues.queuebase import Queue


def hotPotato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)

    print(q.size())

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))












