"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    """
    如果一个节点的右子树不为空，那么该节点的下一个节点是右子树的的最左节点
    否则，向上找第一个左连接指向的树包含该节点的祖先节点
    """
    def GetNext(self, pNode):
        # 特判
        if pNode is None:
            return

        pNext = None
        # 若一个节点的右节点不为空
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode

        # 若一个节点的右节点为空的情况
        else:
            # 当父节点存在且父节点的左节点等于其本身，直接返回父节点
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            # 当父节点存在且父节点的右节点等于其本身
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                if pNode.next:
                    pNext = pNode.next
        return pNext


class Solution2:
    def GetNext(self, pNode):
        # 第一种情况：节点不存在，直接返回空
        if not pNode:
            return None
        # 第二种情况：节点的右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着左子节点找到叶子节点即为下一个节点
        if pNode.right:
            pNode = pNode.next
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 第三种情况：节点不是根节点。如果该节点是其父节点的左孩子，则返回其父节点，否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next
        return None
