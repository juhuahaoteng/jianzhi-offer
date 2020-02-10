"""
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    """排序的数组：二分查找"""
    def GetNumberOfK(self, data, k):
        # 特判
        if not data:
            return 0

        if self.GetLastK(data, k) == -1 and self.GetFirstK(data, k) == -1:
            return 0

        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1

    # 获得数字k在排序数组data中第一次出现的索引位置
    def GetFirstK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if mid == low or data[mid - 1] != k:
                    return mid
                else:
                    high = mid - 1
        return -1

    # 获得数字k在排序数组data中最后出现的索引位置
    def GetLastK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == high or data[mid + 1] != k:
                    return mid
                else:
                    low = mid + 1
        return -1
