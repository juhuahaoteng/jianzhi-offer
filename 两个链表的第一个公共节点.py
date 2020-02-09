"""
输入两个链表，找出它们的第一个公共结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    设A的长度为a+c，B的长度为b+c，其中c为尾部公共部分长度，可知a+c+b == b+c+a。

    当访问链表A的指针访问到链表尾部时，令它从链表B的头部重新开始访问链表B；同样地，当访问链表B的指针访问到链表尾部
    时，令它从链表A的头部重新开始访问链表A。这样就能控制访问A和B的两个链表指针能同时访问到交点。
    """
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 特判
        if not pHead1 or not pHead2:
            return None

        p1, p2 = pHead1, pHead2
        len1 = len2 = 0
        # 遍历链表1，求出其长度len1
        while p1:
            len1 += 1
            p1 = p1.next
        # 遍历链表2，求出其长度len2
        while p2:
            len2 += 1
            p2 = p2.next

        if len1 > len2:
            while len1 - len2:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len2 - len1:
                pHead2 = pHead2.next
                len2 -= 1

        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None
