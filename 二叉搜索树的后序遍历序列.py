"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    """
    递归：先判断数组的左右子树的位置，然后再判读左右子树是不是二叉搜索树
    思路：二叉搜索树的特点是，左子树的值小于根节点，右子树的值大于根节点。后序遍历的话，先遍历左子树，在遍历右子树，最后遍历根节点。
        所以所给序列的最后一个元素为根节点的值。数组的数字可以分为两个部分：第一部分为左子树节点的值，她们都比根节点的值小，第二部分
        为右子树的值，它们都比根节点的值大；值得注意的是，需要考虑只有左子树和只有右子树的情况。
    """
    def VerifySquenceOfBST(self, sequence):
        # 特判
        if sequence == None or len(sequence) == 0:
            return False
        # 数组的长度
        length = len(sequence)
        # 后序遍历中根节点为数组的最后一个值
        root = sequence[-1]
        # 二叉搜索树中左子树节点均小于根节点
        for i in range(length):
            # 循环遍历，从而找到左子树的索引值
            if sequence[i] > root:
                break
        # 二叉搜索树的右子树均大于根节点
        for j in range(i, length):
            # 当右子树中存在一个值小于根节点，则返回false
            if sequence[j] < root:
                return False
        # 判断左子树是否为二叉树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        # 判断右子树是否为二叉树
        right = True
        if j < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])

        return left or right
