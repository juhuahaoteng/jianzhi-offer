"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# -*- coding:utf-8 -*-
class Solution:
    """在字符串尾部填充任意字符，使得字符串的长度等于替换之后的长度。因为一个空格要替换成三个字符，因此当遍历到一个空格时，需要在尾部填充任意两个字符
    令P1指向字符串原来的末尾位置，P2指向字符串现在的末尾位置。P1和P2从后向前遍历，当P1遍历到一个空格时，就需要令P2指向的位置依次填充02%（注意时逆序的）
    否则就填充上P1指向的值。从后向前上是为了在改变P2所指向的内容时，不会影响到P1遍历原来的字符串的内容。
    """
    def replaceSpace(self, s):

        if not isinstance(s, str) or len(s) <= 0 or s is None:
            return ''

        spaceNum = 0
        for i in s:
            if i == ' ':
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)

