"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    """
    递归：先判断数组的左右子树的位置，然后再判读左右子树是不是二叉搜索树
    """
    def VerifySquenceOfBST(self, sequence):

        if sequence == []:
            return False

        length = len(sequence)
        root = sequence[-1]

        for i in range(length):
            if sequence[i] > root:
                break

        for j in range(i, length):
            if sequence[j] < root:
                return False

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if j < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])

        return left or right
