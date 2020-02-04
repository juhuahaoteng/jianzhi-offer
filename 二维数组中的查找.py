"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# -*- coding:utf-8 -*-
class Solution:
    """二维数组中的任意一个数，它左边的数都比它小，它上边的数都比它小，所以可以从矩阵的左下方开始出发
    若数大于target，则向上移动，小于target，则向右移动。
    """
    def Find(self, target, array):
        # 行数
        m = len(array)
        # 特判
        if m == 0:
            return False
        n = len(array[0])
        # 最下面一行
        row = m - 1
        # 第一列
        col = 0
        # 遍历数组，当行大于等于0，列小于n
        while row >= 0 and col < n:
            # 当target小，则向上移动
            if array[row][col] > target:
                row -= 1
            # 当target大，则向右移动
            elif array[row][col] < target:
                col += 1
            else:
                return True
        return False

