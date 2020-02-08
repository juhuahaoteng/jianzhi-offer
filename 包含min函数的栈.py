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
        # write code here
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        # write code here
        if self.stack is None or self.minStack is None:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]
