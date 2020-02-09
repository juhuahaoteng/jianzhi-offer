"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


class Solution:
    """
    可以看成为一个排序问题，在比较两个字符串S1和S2的大小时，应该比较的时S1+S2和S2+S1的大小，
    如果S1+S2< S2+S1，那么应该把S1排在前面，否则把S2排在前面
    """
    def PrintMinNumber(self, numbers):

        if not numbers:
            return ''

        str_num = [str(m) for m in numbers]
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    str_num[i], str_num[j] = str_num[j], str_num[i]

        return ''.join(str_num)
