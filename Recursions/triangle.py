# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          triangle
# Author:        xiaohuo
# Date:          2020/4/3
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:01 
# -------------------------------------------------------------------------------
from turtle import *

"""
python实现谢尔平斯基三角形
"""


def drawTriangle(points, color, myTurtle):
    """
    生成谢尔平斯基三角形
    :param points: 分割的次数
    :param color: 三角形的颜色
    :param myTurtle: turtle的对象
    :return: None
    """
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()


def getMid(p1, p2):
    """
    接受两个点作为输入，并返回它们的中点
    :param p1:第一个点
    :param p2:第二个点
    :return:两个点的中点
    """
    return ((p1[0]+p2[0]) /2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    """
    绘画三角形
   :param points: 分割的次数
    :param colorIndex: 三角形的颜色下标
    :param myTurtle: turtle的对象
    :return:None
    """
    colorlist = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colorlist[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]),getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]),getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]),getMid(points[0], points[2])], degree-1, myTurtle)


if __name__ == '__main__':
    myTurtle = Turtle()
    mywin = myTurtle.getscreen()
    myPoints = [(-500, -250), (0, 500), (500, -250)]
    sierpinski(myPoints, 5, myTurtle)
    mywin.exitonclick()
