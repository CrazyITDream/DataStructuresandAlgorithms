# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          towerOfHanoi
# Author:        xiaohuo
# Date:          2020/4/3
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   21:47 
# -------------------------------------------------------------------------------
"""
python解决汉诺塔的问题
"""
from Stack.stack import Stack


def moveTower(height, fromPole, toPole, withPole):
    """
    汉诺塔的问题
    :param height: 有圆圈的柱子高度
    :param fromPole: 从那根柱子开始运动
    :param toPole: 移动到那根柱子
    :param withPole: 变量的柱子
    :return: None
    """
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(tp, fp):
    """
    打印移动过程
    :param tp: 移动圆圈到tp柱子上
    :param fp: 从fp移动圆圈到tp柱子上
    :return: None
    """
    print("moving  disk from %s to %s" % (fp, tp))


if __name__ == '__main__':
    # stack1 = Stack()
    # stack2 = Stack()
    # stack3 = Stack()
    # moveTower(5, stack1, stack2, stack3)      # 使用栈来保存状态
    moveTower(5, 1, 2, 3)           # 未使用栈保存状态









