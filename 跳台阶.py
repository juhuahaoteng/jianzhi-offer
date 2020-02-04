"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


class Solution:
    """本题就是斐波那契数列：f(n) = f(n - 1) + f(n - 2)"""
    def jumpFloor(self, number):
        #
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number+1) % 2]
