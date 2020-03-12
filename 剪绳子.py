"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）
示例1
    输入: 8
    输出: 18
"""


class Solution:
    """动态规划"""
    def cutRope(self, number):
        # 特判
        if number < 2:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2

        max_list = [0, 1, 2]

        for i in range(3, number + 1):
            if i < number:
                max_num = i
            else:
                max_num = 0
            for j in range(1, i // 2 + 1):
                tmp = max_list[j] * max_list[i - j]
                if tmp > max_num:
                    max_num = tmp
            max_list.append(max_num)
        return max_list[number]


class Solution2:
    def cutRope(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number == 3:
            return 2

        max_list = [0, 1, 2, 3]
        for i in range(4, number+1):
            max = 0
            for j in range(1, i):
                temp = max_list[i] * max_list[i - j]
                if temp > max:
                    max = temp
            max_list.append(max)
        return max_list[-1]
