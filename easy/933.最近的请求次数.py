#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
from collections import deque


class RecentCounter:
    # Time Limit Exceeded

    # def __init__(self):
    #     self.count = 0
    #     self.inputs = []

    # def ping(self, t: int) -> int:
    #     count = 0
    #     self.inputs.append(t)
    #     for input in self.inputs:
    #         if t-3000 <= input <= t:
    #             count += 1
    #     return count

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
