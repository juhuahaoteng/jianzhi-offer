"""
题目描述
    请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
    如果当前字符流没有存在出现一次的字符，返回#字符。
"""


# -*- coding:utf-8 -*-
class Solution:
    """
    将字符流保存下来，通过哈希表统计字符流中每个字符出现的次数，顺便将字符流保存在string中，然后在遍历
    string，从哈希表中找到第一个出现一次的字符。
    """
    def __init__(self):
        self.dic = {}
        self.lis = []

    def FirstAppearingOnce(self):
        # write code here
        while len(self.lis) > 0 and self.dic[self.lis[0]] == 2:
            self.lis.pop(0)
        if len(self.lis) == 0:
            return '#'
        else:
            return self.lis[0]

    def Insert(self, char):
        # write code here
        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lis.append(char)
        elif self.dic[char]:
            self.dic[char] = 2

