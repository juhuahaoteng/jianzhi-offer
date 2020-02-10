"""
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""


class Solution:
    def FindContinuousSequence(self, tsum):

        small, big, res = 1, 2, []
        csum = small + big
        while small < big:
            if csum > tsum:
                csum -= small
                small += 1
            else:
                if csum == tsum:
                    res.append([i for i in range(small, big+1)])
                big += 1
                csum += big
        return res
