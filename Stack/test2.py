# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch3
# Author:        xiaohuo
# Date:          2020/3/29
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   15:18 
# -------------------------------------------------------------------------------
from Stack.stack import Stack
"""
python使用栈将十进制数转换成二进制数
"""


def divideBy2(div_Num, base):
    bin_str = ""
    digits = "0123456789ABCDEF"
    s = Stack()

    while div_Num > 0:
        rem = div_Num % base
        s.push(rem)
        div_Num = div_Num // base

    while not s.isEmpty():
        bin_str += str(digits[s.pop()])

    return bin_str


if __name__ == '__main__':
    print(divideBy2(13, 16))

