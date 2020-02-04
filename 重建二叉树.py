"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    前序遍历的第一个值为根节点的值，使用这个值将中序遍历结果分为两部分，左部分为树的左子树中序遍历
    右部分为树的右子树中序遍历的结果
    """
    def reConstructBinaryTree(self, pre, tin):
        # 特判
        if not pre and not tin:
            return None
        # 前序遍历的第一个值为根节点
        root = TreeNode(pre[0])
        # 当前序遍历与中序遍历的集合值不同，直接返回None
        if set(pre) != set(tin):
            return None
        # 找到根节点在中序遍历的索引值
        i = tin.index(pre[0])
        # 递归
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root
