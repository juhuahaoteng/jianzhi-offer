"""
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    先交换根节点的两个子节点，在交换这两个子节点的左右子节点
    """
    def Mirror(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return root

        ptemp = root.left
        root.left = root.right
        root.right = ptemp

        self.Mirror(root.left)
        self.Mirror(root.right)
