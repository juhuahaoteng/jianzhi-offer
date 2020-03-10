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
        # 当没有根节点或者根节点的值大于expectNumber的值，直接返回空列表
        if not root or root.val > expectNumber:
            return []
        # 当只有根节点且根节点的值等于expectNumber，直接返回根节点列表
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        # 否则
        else:
            expectNumber -= root.val
            # 递归调用root的左节点
            left = self.FindPath(root.left, expectNumber)
            # 递归调用root的右节点
            right = self.FindPath(root.right, expectNumber)
            # 使用列表推导式保存节点值
            result = [[root.val] + i for i in left]
            for i in right:
                result.append([root.val] + i)
        # 排序result列表
        return sorted(result, key=lambda x: -len(x))
