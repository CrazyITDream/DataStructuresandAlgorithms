# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          RecursionVisual
# Author:        xiaohuo
# Date:          2020/4/3
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   16:59 
# -------------------------------------------------------------------------------
"""
python使用turtle实现递归可视化
"""
from turtle import *

MyTurtle = Turtle()
myWin = MyTurtle.getscreen()


# def drawSprial(MyTurtle, lineLen):
#     if lineLen > 0:
#         MyTurtle.forward(lineLen)
#         MyTurtle.right(90)
#         drawSprial(MyTurtle, lineLen-5)


def tree(branchLen, t):
    """
    分形树
    :param branchLen:长度
    :param t:对象
    :return:None
    """
    if branchLen > 5:
        t.forward(branchLen)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

# tree(100, MyTurtle)
# myWin.exitonclick()


def tree1():
    MyTurtle.left(90)
    MyTurtle.up()
    MyTurtle.backward(300)
    MyTurtle.down()
    MyTurtle.color('green')
    tree(110, MyTurtle)
    myWin.exitonclick()

tree1()






