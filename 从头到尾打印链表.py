"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """巧用insert()函数"""
    def printListFromTailToHead(self, listNode):
        # 特判
        if not listNode:
            return []

        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res
