"""
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，
请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    """直接利用python的切片功能"""
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]


class Solution2:
    """先翻转整个字符串，在将两个部分分别翻转在拼接在一起。"""
    def LeftRotateString(self, s, n):
        # 特判
        if len(s) <= 0 or n < 0 or len(s) < n:
            return ''

        lis = list(s)
        self.Reverse(lis)
        length = len(s)
        pivot = length - n
        frontlist = self.Reverse(lis[:pivot])
        behindlist = self.Reverse(lis[pivot:])
        res = ''.join(frontlist) + ''.join(behindlist)
        return res

    def Reverse(self, lis):
        if not lis or len(lis) <= 0:
            return ''

        start = 0
        end = len(lis) - 1
        while start < end:
            lis[start], lis[end] = lis[end], lis[start]
            start += 1
            end -= 1
        return lis
