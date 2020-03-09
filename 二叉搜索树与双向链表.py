"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    二叉搜索树的特点是：左节点的值 < 根节点的值 < 右节点的值，不难发现，使用二叉树的中序遍历出来的数据的排序就是排序的顺序
    """
    def Convert(self, head):
        # 特判
        if not head:
            return None
        # 当只有一个根节点时，直接返回根节点即可
        if not head.left and not head.right:
            return head
        # 递归调用根节点的左节点
        self.Convert(head.left)
        # left指针指向根节点的左节点
        left = head.left
        # 当left节点存在时
        if left:
            # 当left节点存在右节点
            while left.right:
                # left指针指向它的右节点，因为在根节点的左节点中，此时的右节点是最大的
                left = left.right
            # 根节点的右节点指向left
            head.left = left
            # 根节点指向left指针的右节点（双向指针），形成双向指针，即双向链表
            left.right = head

        self.Convert(head.right)
        # right指针指向根节点的右节点
        right = head.right
        # 当右节点存在时
        if right:
            # 当右节点存在子左节点时
            while right.left:
                # 循环直至找到最右节点的左节点
                right = right.left
            # 将根节点的右节点与这个节点相连
            head.right = right
            # 反向相连，形成双向指针（双向链表）
            right.left = head
        # 当根节点存在左节点时
        while head.left:
            # 递归调用，直至找到最左的节点，即将head指针指向根节点的最左的节点，而不是根节点
            # 因为根节点的最左的节点时最小的值，这样就形成了一个排好序的双向链表
            head = head.left

        return head
