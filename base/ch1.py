# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          ch1
# Author:        xiaohuo
# Date:          2020/3/28
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   13:09 
# -------------------------------------------------------------------------------
"""
实现简单的方法 getNum 和 getDen ，它们分别返回分数的分子和分母
"""


class Fraction:
    def __init__(self, top, bottom):
        self.num = top          # 分子
        self.den = bottom       # 分母

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):           # 化简分数
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num

        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):                #
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n


f1 = Fraction(1, 4)
Fraction.__add__(f1)
print(f1.getNum())
print(f1.getDen())
f2 = Fraction(2, 3)
f2.show()
print(f2.getNum())
print(f2.getDen())




























































