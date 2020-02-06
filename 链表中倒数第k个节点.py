"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    设链表的长度位N，两个指针p1和p2，先让p1移动K个节点，则还有N-K个节点可以移动。此时让p1和p2同时移动，
    可以直到当p1移动到链表结尾，p2移动到N-K个节点处，该位置就是倒数第K个节点。
    """
    def FindKthToTail(self, head, k):
        # 特判
        if not head or k <= 0:
            return None

        pAhead = head

        for i in range(k - 1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None

        pBhead = head
        while pAhead.next:
            pAhead = pAhead.next
            pBhead = pBhead.next
        return pBhead
