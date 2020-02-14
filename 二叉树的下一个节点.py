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
        # write code here
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
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                if pNode.next:
                    pNext = pNode.next
        return pNext
