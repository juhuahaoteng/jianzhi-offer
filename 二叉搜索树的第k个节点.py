"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """利用二叉搜索树的中序遍历来解决"""
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return
        res = []

        def traverse(node):
            if len(res) >= k or not node:
                return
            traverse(node.left)
            res.append(node)
            traverse(node.right)

        traverse(pRoot)
        if len(res) < k:
            return
        return res[k - 1]

