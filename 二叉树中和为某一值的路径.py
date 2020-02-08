"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """深度优先搜索"""
    def FindPath(self, root, expectNumber):

        if not root or root.val > expectNumber:
            return []

        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]

        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)

            result = [[root.val] + i for i in left]
            for i in right:
                result.append([root.val] + i)

        return sorted(result, key=lambda x: -len(x))
