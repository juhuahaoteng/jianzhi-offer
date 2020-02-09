"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    二叉搜索树的特点是：左节点的值 < 根节点的值 < 右节点的值，不难发现，使用二叉树的中序遍历出来的数据的排序就是排序的顺序
    """
    def Convert(self, pRootOfTree):

        if not pRootOfTree:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        if left:
            while left.right:
                left = left.right

            pRootOfTree.left = left
            left.right = pRootOfTree

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        if right:
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left = pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree
