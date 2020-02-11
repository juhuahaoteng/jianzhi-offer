"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


class Solution:
    """
    a ^ b表示没有考虑进位的情况下两数的和，而( a & b) << 1表示进位。
    递归终止的原因是：( a & b) << 1最右边会多出一个0，那么递归继续，进位最右边的0会慢慢增多，最后进位会变成0，递归终止。
    """
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296
