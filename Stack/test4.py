# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch5
# Author:        xiaohuo
# Date:          2020/3/29
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:57 
# -------------------------------------------------------------------------------
"""
python实现计算后序表达式
"""
from Stack.stack import Stack


def postfixEval(operandStrack, tokenList, operand, operateSymbol):
    """
    利用栈进行计算
    :param operandStrack:栈的对象
    :param tokenList:表达式列表
    :param operand:操作数
    :param operateSymbol:操作符
    :return:计算结果
    """
    for token in tokenList:
        if token in operand:  # 判断是否为操作数
            operandStrack.push(int(token))
        if token in operateSymbol:  # 判断是否为操作符
            if not operandStrack.isEmpty():  # 判断栈是否为空
                operand_1 = operandStrack.pop()
                operand_2 = operandStrack.pop()
                result = calculate(operand_1, operand_2, token)
                operandStrack.push(result)

    return operandStrack.pop()


def calculate(num1, num2, symbol):
    """
    操作数的计算
    :param num1:操作数1
    :param num2:操作数2
    :param symbol:操作符
    :return:计算后的结果
    """
    if symbol == '+':
        return num1 + num2
    if symbol == '-':
        return num1 - num2
    if symbol == '*':
        return num1 * num2
    if symbol == '/':
        return num1 / num2
    else:
        return None


def simplification(postfixExpr, operand):
    """
    对输入表达式判断以及分类
    :param postfixExpr:输入的表达式
    :param operand:生成的操作数列表
    :param operateSymbol:操作符列表
    :return:处理后的表达式列表
    """
    tokenLists = []
    operateSymbol_list = ['+', '-', '*', '/', '(', ')']
    for i in list(postfixExpr):
        if i in operand or i in operateSymbol_list:
            tokenLists.append(i)
        elif i == ' ':
            pass
        else:
            raise Exception("你输入的不是操作数(0-9)或者操作符(+-*/),你的输入为:%s", format(i))
    return tokenLists


def create_Target():
    """
    生成Strack的对象
    :return:Strack的对象
    """
    return Stack()


def create_operand():
    """
    生成操作数和定义操作符
    :return:操作数(operand)、操作符(operateSymbol)
    """
    operand = list(str(i) for i in range(10))  # 生成0至9操作数
    operateSymbol = ['+', '-', '*', '/']  # 操作符
    return operand, operateSymbol


if __name__ == '__main__':
    postfixExpr = input("请输入要计算的后序表达式:")
    operandStrack = create_Target()  # 操作栈对象
    operand, operateSymbol = create_operand()
    tokenLists = simplification(postfixExpr, operand)
    print(str("".join(tokenLists)) + "=" + str(postfixEval(operandStrack, tokenLists, operand, operateSymbol)))
