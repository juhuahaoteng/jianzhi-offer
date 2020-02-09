"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    """
    1、在每个节点的后面插入复制的节点
    2、在复制节点的random链接进行复制
    3、拆分
    """
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        pNode = pHead

        while pNode:
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

        pNode = pHead

        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next

        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneHead.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead
