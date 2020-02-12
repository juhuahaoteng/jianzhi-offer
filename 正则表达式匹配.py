"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):

        memo = dict()

        def dp(i, j):
            """

            :param i: 表示当前s的匹配位置
            :param j: 表示当前p的匹配位置
            :return:
            """
            if (i, j) in memo:
                return memo[(i, j)]
            # 表示p已经匹配完了，若s还有字符尚未匹配则返回False，否则表示s也已经匹配完成，返回True
            if j == len(pattern):
                return i == len(s)
            # first表示当前s，p的首位是否匹配，p[j]是否为s[i]或是星号
            # i < len(s）表示s是否遍历完
            first = i < len(s) and pattern[j] in {s[i], '.'}
            # 当j中存在星号且j的长度小于总长度减2
            if j <= len(pattern) - 2 and pattern[j + 1] == '*':
                # 跳过这两个字符，表示匹配0次
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                # 若j中不存在星号时，继续向后匹配
                ans = first and dp(i + 1, j + 1)
            # 缓存值备忘录
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
