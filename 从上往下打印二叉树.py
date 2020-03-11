"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """当开始遍历一层的节点时，当前队列中的节点数就是当前层的节点数，只要控制遍历的节点数，就可以保证只遍历当前层"""
    def PrintFromTopToBottom(self, root):
        # 特判
        if root is None:
            return []

        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)

        return result
