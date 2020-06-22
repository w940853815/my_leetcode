#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 任务调度器
#


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.queue:
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.queue) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) == self.size
