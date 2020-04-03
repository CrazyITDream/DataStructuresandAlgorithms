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

    for token in tolist(infixexpr):
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
            elif token in operator_list:  # 判断是否是运算符
                while not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token]):
                    result.append(opstack.pop())
                opstack.push(token)
            else:
                pass

    while not opstack.isEmpty():
        result.append(opstack.pop())

    return "".join(result)


def tolist(need_transition_str):
    """
    将输入的字符转换成列表，返回
    :param need_transition_str:输入的字符
    :return:转换成列表
    """
    return [transition_str.upper() for transition_str in need_transition_str if transition_str != " "]


def judge(transition_str):
    operator_list = ['+', '-', '*', '/', '(', ')']
    digit_list = [str(i) for i in range(0, 10)]
    transition_str_judge = ""
    for str_judge in transition_str:
        if str_judge in digit_list:
            raise Exception("你输入了非字母%s，请重新输入" % (str_judge))
        elif str_judge.isalpha() or str_judge in operator_list:
            transition_str_judge += str_judge
        else:
            raise Exception("你输入了非计算字符%s,请检查重新输入!!" % (str_judge))

    return transition_str_judge


if __name__ == '__main__':
    transition_str_input = input("请输入要转换为后序字符串：")
    print(infixToPostfix(judge(transition_str_input)))
