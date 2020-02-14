"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归法"""
    def isSymmetrical(self, pRoot):
        # write code here
        return self.selfIsSym(pRoot, pRoot)

    def selfIsSym(self, root1, root2):
        # 当两个都为空，返回True
        if root1 is root2 and root2 is None:
            return True
        # 当其中一个为空，返回False
        if root1 is None or root2 is None:
            return False
        # 当两个节点的值不相等的情况，返回False
        if root1.val != root2.val:
            return False

        return self.selfIsSym(root1.left, root2.right) and self.selfIsSym(root1.right, root2.left)
