# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            val = self.stack.pop()
            self.stack2.append(val)
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1
