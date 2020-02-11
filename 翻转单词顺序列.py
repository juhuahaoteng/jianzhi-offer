"""
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，
但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""


class Solution:
    """先旋转每个单词，在旋转整个字符串"""
    def ReverseSentence(self, s):
        # 特判
        if not s or len(s) <= 0:
            return ''

        lis = list(s)
        lis = self.Reverse(lis)
        start = 0
        end = 0
        res = ''
        # 临时保存单个翻转单词
        lisTmp = []
        while end < len(s):
            if end == len(s) - 1:
                lisTmp.append(self.Reverse(lis[start:]))
                break
            if lis[start] == ' ':
                start += 1
                end += 1
                lisTmp.append(' ')
            elif lis[end] == ' ':
                lisTmp.append(self.Reverse(lis[start:end]))
                start = end
            else:
                end += 1
        for i in lisTmp:
            res += ''.join(i)
        return res

    def Reverse(self, lis):
        """翻转单词"""
        # 特判
        if not lis or len(lis) <= 0:
            return ''

        start = 0
        end = len(lis) - 1
        while start < end:
            lis[start], lis[end] = lis[end], lis[start]
            start += 1
            end -= 1
        return lis
