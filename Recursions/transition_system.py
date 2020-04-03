# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          transition_system
# Author:        xiaohuo
# Date:          2020/4/3
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   15:46 
# -------------------------------------------------------------------------------
from Stack.stack import Stack


class transition:
    def __init__(self):
        self.stack = Stack()
        self.base_str = ""

    def toStr(self, num, base):
        """
        使用栈帧递归将任何数转换成进制数
        :param num: 转换的数
        :param base: 进制数
        :return: 转换之后的数
        """
        coverString = "0123456789ABCDEF"
        if num < base:
            self.stack.push(coverString[num])
        else:
            self.stack.push(coverString[num % base])
            self.toStr(num//base, base)

    def show(self):
        for i in range(self.stack.size()):
            self.base_str += self.stack.pop()
        print(self.base_str)
        # return self.base_str


if __name__ == '__main__':
    t = transition()
    t.toStr(10, 2)
    t.show()













