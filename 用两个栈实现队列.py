"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        # stack1完成入栈操作
        self.stack1 = []
        # stack2完成出栈操作
        self.stack2 = []

    def push(self, node):
        # stack1完成入栈操作
        self.stack1.append(node)

    def pop(self):
        # 当两个栈都为空，操作结束
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        # 当出栈的stack2为空时
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                # 出栈的stack2压入stack1的元素
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
