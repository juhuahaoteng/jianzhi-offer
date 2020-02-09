"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    """
    多数投票问题：可以利用Boyer-Moore Majority Vote Algorithm来解决这个问题。使得时间复杂度为O(N)

    使用cnt来统计一个元素的出现次数，当遍历的元素与统计的元素相等时，令cnt++，否则令cnt--。如果前面查找了i个元素，且cnt==0，
    说明前i个元素没有majority或者右majority但是出现的次数小于i/2，因此，如果多余i/2的话，cnt就一定不会为0。此时，剩下的n-i个
    元素中，majority的数目依然多于(n-i)/2，因此，继续查找就能找到majority。
    """
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers:
            return 0
        result = numbers[0]
        times = 1

        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckNoreThanHalf(numbers, length, result):
            return 0
        return result

    def CheckNoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True
