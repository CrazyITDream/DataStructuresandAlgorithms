# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch1
# Author:        xiaohuo
# Date:          2020/3/28
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:44 
# -------------------------------------------------------------------------------
"""
利用python的列表模拟对栈的操作
"""

'''
class Stack:
    # 假设栈的顶部就是列表的尾部
    def __init__(self):
        self.item = []

    def push(self, item):
        """
        模拟栈在顶端添加元素
        :param item:添加的元素
        :return:
        """
        self.item.append(item)

    def pop(self):
        """
        模拟栈删除顶端元素
        :return: 删除之后的元素
        """
        return self.item.pop()

    def peek(self):
        """
        模拟栈获取顶端元素
        :return:
        """
        return self.item[0] if len(self.item) == 1 else self.item[len(self.item)-1]
        # return self.item[len(self.item)-1]

    def isEmpty(self):
        """
        模拟判断栈是否为空
        :return:
        """
        return self.item == []

    def size(self):
        """
        模拟获取栈的长度
        :return:
        """
        return len(self.item)


if __name__ == '__main__':
    s = Stack()
    # 判断栈是否为空
    print('为空' if s.isEmpty() else '不为空')       # 三元运算符

    # 添加元素
    s.push(2)
    s.push('dog')
    # 获取栈顶元素
    print("栈顶元素为:"+s.peek())
    # 获取栈的元素个数
    print("栈中一共有:"+str(s.size())+"个元素")
    # 添加元素
    s.push(True)

    # 获取栈的元素个数
    print("栈中一共有:"+str(s.size())+"个元素")

    # 删除栈顶元素
    print(s.pop())

    # 获取上除后栈的长度
    print("栈中还剩下:"+str(s.size())+"个元素")

'''
class Stack:
    # 假设栈的顶部为列表的头部
    def __init__(self):
        # 定义列表
        self.item = []

    def isEmpty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.item == []

    def push(self, item):
        """
        添加元素到栈顶
        :return:
        """
        return self.item.insert(0, item)

    def pop(self):
        """
        删除栈顶元素
        :return:
        """
        return self.item.pop(0)

    def peek(self):
        """
        获取栈顶元素
        :return:
        """
        return self.item[0]

    def isEmpty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.item == []

    def size(self):
        """
        获取栈的元素个数
        :return:
        """
        return len(self.item)


# if __name__ == '__main__':
#     s = Stack()
#     # 判断栈是否为空
#     print('为空' if s.isEmpty() else '不为空')       # 三元运算符
#
#     # 添加元素
#     s.push(2)
#     s.push('dog')
#     # 获取栈顶元素
#     print("栈顶元素为:"+s.peek())
#     # 获取栈的元素个数
#     print("栈中一共有:"+str(s.size())+"个元素")
#     # 添加元素
#     s.push(True)
#
#     # 获取栈的元素个数
#     print("栈中一共有:"+str(s.size())+"个元素")
#
#     # 删除栈顶元素
#     print('删除成功' if s.pop() else '删除不成功')
#
#     # 获取上除后栈的长度
#     print("栈中还剩下:"+str(s.size())+"个元素")












