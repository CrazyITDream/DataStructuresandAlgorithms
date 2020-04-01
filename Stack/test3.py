# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch4
# Author:        xiaohuo
# Date:          2020/3/29
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   19:37 
# -------------------------------------------------------------------------------
"""
用 Python实现从中序表达式到后序表达式的转换
"""
from Stack.stack import Stack
import string


def infixToPostfix(infixexpr):
    opstack = Stack()  # 创建空栈
    result = []  # 结果的列表
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # 运算符的优先级
    operator_list = ['+', '-', '*', '/']

    tokenList = list(infixexpr)  # 将输入的字符串转化为列表

    for token in tokenList:
        if token.capitalize() in string.ascii_uppercase:  # 判断是否是操作数
            result.append(token.capitalize())
        else:
            if token == '(':  # 判断是是否是左括号
                opstack.push(token)
            elif token == ')':  # 判断是否是右括号
                topToken = opstack.pop()
                while topToken != '(':
                    result.append(topToken)
                    topToken = opstack.pop()
            elif token in operator_list:    # 判断是否是运算符
                while not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token]):
                    result.append(opstack.pop())
                opstack.push(token)
            else:
                pass

    while not opstack.isEmpty():
        result.append(opstack.pop())

    return "".join(result)


if __name__ == '__main__':
    print(infixToPostfix('(A+B)*(C+D)'))
