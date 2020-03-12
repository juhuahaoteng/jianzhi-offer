"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    """
    使用两个栈，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据，辅助栈用于储存最小值。
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # 先将节点压入数据栈中
        self.stack.append(node)
        # 判断最小栈是否为空或者节点值小于当前最小值
        if self.minStack == [] or node < self.min():
            # 压入最小栈中
            self.minStack.append(node)
        # 否则
        else:
            temp = self.min()
            # 最小栈压入刚弹出的最小值
            self.minStack.append(temp)

    def pop(self):
        # 判断这个数据栈为空或者最小栈为空，直接返回
        if self.stack is None or self.minStack is None:
            return None
        # 否则正常弹出数值
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        # 返回数据占的最上面的值
        return self.stack[-1]

    def min(self):
        # 返回最小栈的最上面的值
        return self.minStack[-1]
