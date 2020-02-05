"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""


class Solution:
    """
    x ^ n = (x * x) ** (n/2)     n % 2 == 0
          = x * (x * x) ** (n/2) n % 2 == 1

    因为(x*x) ** n/2可以通过递归求解，并且每次递归n都减小一半，因此整个算法的时间复杂度为O(log(n))
    """
    def Power(self, base, exponent):
        res = self.power_value(base, abs(exponent))
        if exponent < 0:
            return 1.0 / res
        else:
            return res

    def power_value(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.power_value(base, exponent >> 1)
        res *= res
        # 若exponent为奇数，还需再乘以base
        if exponent & 1 == 1:
            res *= base
        return res
