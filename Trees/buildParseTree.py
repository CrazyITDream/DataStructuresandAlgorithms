# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          buildParseTree
# Author:        xiaohuo
# Date:          2020/4/15
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   9:09 
# -------------------------------------------------------------------------------
"""
python实现构建解析器
"""

from Stack.stack import Stack
from Trees.nodeBinaryTree import Tree


class builderParseTree:
    """
    利用栈的先进后出特性和树构建解析时并计算
    """

    def __init__(self, fpexp):
        """
        初始化变量，创建栈和树的对象
        :param fpexp: 表达式
        """
        self.fpexp = fpexp
        self.pStack = Stack()
        self.eTree = Tree('')

    def builderParseTree(self):
        """
        构建解析树
        :return: 树
        """
        fplist = self.fpexp.split()
        self.pStack.push(self.eTree)
        currentTree = self.eTree
        for i in fplist:
            if i == '(':
                currentTree.insertLeft('')
                self.pStack.push(currentTree)
                currentTree = currentTree.getLeftNode()
            elif i not in '+-*/':
                currentTree.setRootValue(eval(i))
                currentTree = self.pStack.pop()
            elif i in '+-*/':
                currentTree.setRootValue(i)
                currentTree.insertRight('')
                self.pStack.push(currentTree)
                currentTree = currentTree.getRightNode()
            elif i == ')':
                currentTree = self.pStack.pop()
            else:
                raise ValueError("Unknow Operator:" + i)

        return self.eTree


if __name__ == '__main__':
    bpt = builderParseTree('((7+3)*(5-2))')
    print(bpt.builderParseTree().getRootValue())
