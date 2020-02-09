"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""


class Solution:
    """递归"""
    def Permutation(self, ss):
        # 字符串为空
        if not ss:
            return []
        # 字符串长度为1的情况
        if len(ss) == 1:
            return list(ss)
        # 字符串转list后再排序
        charList = list(ss)
        charList.sort()
        # 保存结果
        pStr = []
        for i in range(len(charList)):
            # 字符重复的情况，直接跳过
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            # 递归
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))

            for j in temp:
                pStr.append(charList[i] + j)

        return pStr
