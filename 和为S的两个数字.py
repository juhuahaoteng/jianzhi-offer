"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。

"""


class Solution:
    """
    双指针
    """
    def FindNumbersWithSum(self, array, tsum):
        # 特判
        if not array or not tsum:
            return []

        start = 0
        end = len(array) - 1
        while start < end:
            csum = array[start] + array[end]
            if csum < tsum:
                start += 1
            elif csum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]
        return []
