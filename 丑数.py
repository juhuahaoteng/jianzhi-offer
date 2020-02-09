"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):

        if not index:
            return 0

        ugly_number = [1] * index
        next_index = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while next_index < index:
            minValue = min(ugly_number[index2] * 2, ugly_number[index3] * 3, ugly_number[index5] * 5)
            ugly_number[next_index] = minValue

            while ugly_number[index2] * 2 <= ugly_number[next_index]:
                index2 += 1

            while ugly_number[index3] * 3 <= ugly_number[next_index]:
                index3 += 1

            while ugly_number[index5] * 5 <= ugly_number[next_index]:
                index5 += 1

            next_index += 1

        return ugly_number[-1]
