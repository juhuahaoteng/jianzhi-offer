"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    两个栈：打印某一行节点时，把下一层的子节点保存在相应的栈里面。如果当前打印的是奇数层，则先保存左子树节点再保存右子树节点到第一个栈里面，
    如果当前打印的是偶数层，则先保存右子树的节点再保存左子树节点到第二个栈里面。
    """
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        # 是否是从左往右打印，True表示正确
        right = True
        while nodes:
            # 两个栈
            curStack, nextStack = [], []
            # 当从左往右打印时
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            # 当从右往左打印时
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
        return result
