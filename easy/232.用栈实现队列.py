#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            return self.data.pop(0)
        else:
            raise Exception('queue is empty')

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            return self.data[0]
        else:
            raise Exception('queue is empty')

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) <= 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
