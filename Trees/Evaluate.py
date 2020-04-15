# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          Evaluate
# Author:        xiaohuo
# Date:          2020/4/15
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   13:28 
# -------------------------------------------------------------------------------
"""
python实现递归计算表达式
"""


class operator:
    def add(self, num1, num2):
        return num2 + num1

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def truediv(self, num1, num2):
        if num2 == 0:
            raise ValueError("分母不为零", num2)
        else:
            return num1 / num2


def evaluate(paeseTree):
    """
    递归实现计算二叉树
    :param paeseTree:
    :return:
    """
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv
             }
    leftValue = paeseTree.getLeftNode()
    rightValue = paeseTree.getRightNode()

    if leftValue and rightValue:
        fn = opers[paeseTree.getRootValue()]
        return fn(evaluate(leftValue), evaluate(rightValue))
    else:
        return paeseTree.getRootValue()












