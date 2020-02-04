"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


class Solution:
    """如果使用递归求解会重复计算一些子问题。但是使用动态规划会将子问题的解缓存起来，从而避免重复计算求解子问题"""
    def Fibonacci(self, n):

        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]
        return tempArray[n % 2]
