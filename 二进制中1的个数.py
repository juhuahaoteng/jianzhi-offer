"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):

        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            # 去除n的中最低的那一位
            n &= n - 1
        return count
