"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


class Solution:
    """递归"""
    def Sum_Solution(self, n):

        return self.sumN(n)

    def sum0(self, n):
        return 0

    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}
        return n + fun[not not n](n - 1)


class Solution2:
    def Sum_Solution(self, n):
        return n and self.Sum_Solution(n - 1) + n
