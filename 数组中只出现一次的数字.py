"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


class Solution:
    """
    哈希表
    """
    def FindNumsAppearOnce(self, array):
        # 创建一个字典，key为array的值，value记录它在array中出现的次数
        hash_table = dict()
        for num in array:
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1

        result = []
        for key, value in hash_table.items():
            # 当字典的value等于1时，表示只出现一次的情况
            if value == 1:
                result.append(key)
        return result


class Solution2:
    """
    两个不相等的元素在位级表示上必定会有一位存在不同，将数组的所有元素异或得到的结果为不存在重复的两个元素的结果。
    """
    def FindNumsAppearOnce(self, array):

        if array is None:
            return []

        xor = 0
        for i in array:
            xor ^= i

        idxOf1 = self.getFirstIdx(xor)
        num1 = num2 = 0
        for j in range(len(array)):
            if self.IsBit(array[j], idxOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def getFirstIdx(self, num):
        idx = 0
        while num & 1 == 0 and idx <= 32:
            idx += 1
            num = num >> 1
        return idx

    def IsBit(self, num, indexBit):
        num = num >> indexBit
        return num & 1
