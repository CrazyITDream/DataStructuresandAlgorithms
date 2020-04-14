# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          BinaryTree
# Author:        xiaohuo
# Date:          2020/4/14
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   9:51 
# -------------------------------------------------------------------------------

"""
python实现树的操作
"""


class Tree:
    def createBinaryTree(self, r):
        """
        创建二叉树
        :param r:根节点
        :return:创建的树
        """
        return [r, [], []]

    def insertLeft(self, root, newBranch):
        """
        插入数据至左子树
        :param root: 根节点
        :param newBranch: 插入的数据
        :return: 二叉树
        """
        tmp = root.pop(1)
        if len(tmp) > 1:
            root.insert(1, [newBranch, [], tmp])
        else:
            root.insert(1, [newBranch, [], []])
        return root

    def insertRight(self, root, newBranch):
        """
        插入数据到右子树
        :param root: 根节点
        :param newBranch: 插入的元素
        :return: 二叉树
        """
        tmp = root.pop(2)
        if len(tmp) > 1:
            root.insert(2, [newBranch, [], tmp])
        else:
            root.insert(2, [newBranch, [], []])

        return root

    def getRootValue(self, root):
        """
        获取根节点的数据
        :param root:
        :return:
        """
        return root[0]

    def getLeftValue(self, root):
        """
        获取左子树
        :param root:二叉树
        :return: 左子树
        """
        return root[1]

    def getRightValue(self, root):
        """
        获取右子树
        :param root:二叉树
        :return: 右子树
        """
        return root[2]

    def setRootValue(self, root, rootValue):
        """
        设置二叉树的根节点的值
        :param root: 二叉树
        :param rootValue: 根节点的值
        :return: None
        """
        root[0] = rootValue


if __name__ == '__main__':
    tree = Tree()
    r = tree.createBinaryTree(3)     # 创建二叉树
    print(tree.insertLeft(r, 4))
    print(tree.insertRight(r, 5))

































