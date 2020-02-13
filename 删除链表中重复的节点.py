"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

"""


# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """递归法"""
    def deleteDuplicates(self, pHead):
        if not pHead:
            return pHead

        if pHead.next and pHead.val == pHead.next.val:
            while pHead.next and pHead.val == pHead.next.val:
                pHead = pHead.next
            return self.deleteDuplicates(pHead.next)
        else:
            pHead.next = self.deleteDuplicates(pHead.next)
        return pHead


class Solution2:
    """迭代 快慢指针,用快指针跳过那些有重复数组,慢指针负责和快指针拼接"""
    def deleteDuplicates(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        dummy = ListNode(-1)
        dummy.next = pHead
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next

