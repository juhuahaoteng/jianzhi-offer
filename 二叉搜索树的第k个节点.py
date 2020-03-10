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
            # 当列表长度大于k或者不存在node节点
            if len(res) >= k or not node:
                # 返回none
                return
            # 中序遍历
            traverse(node.left)
            res.append(node)
            traverse(node.right)
        # 遍历二叉树
        traverse(pRoot)
        # 当遍历二叉搜索树后形成的数组的长度小于k时
        if len(res) < k:
            return
        return res[k - 1]

