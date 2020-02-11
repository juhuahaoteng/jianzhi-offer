"""
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
    输入一个字符串,包括数字字母符号,可以为空
输出描述:
    如果是合法的数值表达则返回该数字，否则返回0

输入：+2147483647
    1a33
输出：2147483647
    0
"""


class Solution:
    """
    这道题要考虑全面，对异常值要做处理
    1、指针是否为空指针，以及字符串是否为空字符串
    2、字符串对于正负号的处理
    3、输入值是否为合法值，即小于9大于0
    4、int为32为，需要判断是否溢出
    5、使用错误标志，区分合法值与非合法值
    """
    def StrToInt(self, s):
        # write code here
        flag = False
        if not s or len(s) < 1:
            return 0
        num = []
        numdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in numdict.keys():
                num.append(numdict[i])
            elif i == '+' or i == '-':
                continue
            else:
                return 0
        ans = 0
        if len(num) == 1 and num[0] == 0:
            flag = True
            return 0
        for i in num:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = -ans
        return ans


class Solution2:
    def str_to_int(s):
        if not s:  # 空字符返回异常
            raise Exception('string cannot be None', s)
        flag = 0  # 用来表示第一个字符是否为+、-
        ret = 0  # 结果
        for k, v in enumerate(s):
            if v.isdigit():  # 数字直接运算
                val = ord(v) - ord('0')
                ret = ret * 10 + val
            else:
                if not flag:
                    if v == '+' and k == 0:  # 避免中间出现+、-
                        flag = 1
                    elif v == '-' and k == 0:
                        flag = -1
                    else:
                        raise Exception('digit is need', s)
                else:
                    raise Exception('digit is need', s)
        if flag and len(s) == 1:  # 判断是不是只有+、-
            raise Exception('digit is need', s)
        return ret if flag >= 0 else -ret
