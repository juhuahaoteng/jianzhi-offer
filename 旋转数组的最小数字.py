"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    """二分查找，要考虑到数组元素存在重复的情况"""
    def minNumberInRotateArray(self, rotateArray):
        # 特判
        if len(rotateArray) <= 0:
            return 0

        left = 0
        right = len(rotateArray) - 1
        min_val = rotateArray[0]

        if rotateArray[left] < rotateArray[right]:
            return rotateArray[left]
        else:
            while right - left > 1:
                mid = (left + right) // 2
                if rotateArray[mid] >= rotateArray[left]:
                    left = mid
                elif rotateArray[mid] <= rotateArray[right]:
                    right = mid
                # 重复元素的情况
                elif rotateArray[left] == rotateArray[right] == rotateArray[mid]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < min_val:
                            min_val = rotateArray[i]
                            right = i
            min_val = rotateArray[right]
            return min_val
