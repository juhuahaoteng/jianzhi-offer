"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    队列：使用队列来进行层次遍历，不需要使用两个队列来分别存储当前层的节点和下一层的节点，因为在开始遍历一层的节点时，
    当前队列中的节点树就是当前层的节点数，只要控制遍历这么多节点数，就能保证这次遍历的都是当前层的节点。
    """
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodes, res = [pRoot], []
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            res.append(curStack)
            nodes = nextStack
        return res
