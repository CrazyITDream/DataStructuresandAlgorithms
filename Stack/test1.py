# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch2
# Author:        xiaohuo
# Date:          2020/3/29
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   8:48 
# -------------------------------------------------------------------------------
from Stack.stack import Stack


def matches(open, close):
    opens = "( [ {"
    closes = "} ] )"
    return opens.index(open) == closes.index(close)


def parChecker(symbolString):
    """
    普通情况：匹配括号(只有括号的符号)
    :param symbolString:
    :return:
    """
    s = Stack()

    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '( [ {':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):    # false
                    balanced = False
        index += 1
    return True if s.isEmpty() and not balanced else False


if __name__ == '__main__':
    symbol = list('[][][](){}')
    print('匹配字符' if parChecker(symbol) else '不匹配字符')
