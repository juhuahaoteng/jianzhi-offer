"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None

        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead
