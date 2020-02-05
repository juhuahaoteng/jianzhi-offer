"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    """
    数学推导：跳上n-1级台阶，可以从n-2级跳1级上去，也可以从n-3级跳2级上去....，那么：
                f(n-1) = f(n-2) + f(n-3) + ... + f(0)
            同理，跳上n级台阶，可以从n-1级跳1级上去，也可以从n-2级跳2级上去...,那么：
                f(n) = f(n-1) + f(n-2) + f(n -3) + ... + f(0)
            综上所得：
                f(n) - f(n-1) = f(n-1)
            即：
                f(n) = 2 * f(n-1)
    """
    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number - 1):
                ans = ans * 2
        return ans
