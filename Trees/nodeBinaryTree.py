# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          nodeBinaryTree
# Author:        xiaohuo
# Date:          2020/4/14
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   14:36 
# -------------------------------------------------------------------------------
"""
python实现二叉树的构建，使用节点
"""


class Tree:
    def __init__(self, root):
        """
        初始化左右节点和根节点
        :param root:
        """
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        插入数字至左子树中
        :param newNode: 插入的数据
        :return: None
        """
        if self.leftChild == None:
            self.leftChild = Tree(newNode)
        else:
            tmp = Tree(newNode)
            tmp.left = self.leftChild
            self.leftChild = tmp

    def insertRight(self, newNode):
        """
        插入数据到右子树中
        :param newNode: 插入的数据
        :return: None
        """
        if self.rightChild == None:
            self.rightChild = Tree(newNode)
        else:
            tmp = Tree(newNode)
            tmp.right = self.rightChild
            self.rightChild = tmp

    def getLeftNode(self):
        """
        获取左子树
        :return: 左子树
        """
        return self.leftChild

    def getRightNode(self):
        """
        获取右子树
        :return: 右子树
        """
        return self.rightChild

    def setRootValue(self, obj):
        """
        设置根节点的值
        :return: 根节点值
        """
        self.root = obj

    def getRootValue(self):
        """
        获取根节点的值
        :return: 根节点的值
        """
        return self.root

    def preorder(self):
        """
        前序遍历
        :return:
        """
        print(self.root)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

# def preorder(tree):
#     """
#     前序遍历
#     :param tree:
#     :return:
#     """
#     if tree:
#         print(tree.getRootValue())
#         preorder(tree.getLeftNode())
#         preorder(tree.getRightNode())


# def postorder(tree):
#     """
#     后序遍历
#     :param tree:树
#     :return:
#     """
#     if tree != None:
#         postorder(tree.getRightNode())
#         postorder(tree.getLeftNode())
#         print(tree.getRootValue())


# def inorder(tree):
#     """
#     中序遍历
#     :param tree: 树
#     :return:
#     """
#     if tree != None:
#         inorder(tree.getLeftNode())
#         print(tree.getRootValue())
#         inorder(tree.getRightNode())


if __name__ == '__main__':
    tree = Tree('a')
    # print(tree.getRootValue())
    tree.insertLeft('b')
    tree.insertRight('c')
    # print(tree.getLeftNode().getRootValue())
    # print(tree.getRightNode().getRootValue())
    tree.preorder()




























































