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
        # 特判
        if pHead is None or pHead.next is None:
            return pHead
        # 哑节点
        dummy = ListNode(-1)
        # 哑节点指向头节点
        dummy.next = pHead
        # 慢指针
        slow = dummy
        # 快指针
        fast = dummy.next
        # 循环快指针
        while fast:
            # 当快指针的下个节点存在且快指针指向的当前节点与下个节点的值相同时
            if fast.next and fast.next.val == fast.val:
                # 用tmp暂时保存这个值
                tmp = fast.val
                # 循环fast指针时若fast指针在继续移动时，节点值仍然相同
                while fast and tmp == fast.val:
                    # fast指针继续向前移动
                    fast = fast.next
            # 否则
            else:
                # 慢指针向前移动
                slow.next = fast
                # 慢指针移动到快指针指向的节点
                slow = fast
                # 快指针向前移动
                fast = fast.next
        slow.next = fast
        return dummy.next

