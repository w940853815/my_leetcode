#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#
from collections import Counter, defaultdict

# 超出时间限制
# @lc code=start
# class FreqStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> int:
#         if self.stack:
#             count = 0
#             freq_elem = self.stack[0]
#             for s in self.stack[::-1]:
#                 s_count = self.stack.count(s)
#                 if s_count > count:
#                     freq_elem = s
#                     count = s_count
#             new_stack = []
#             pop_val = None
#             for s in self.stack[::-1]:
#                 if pop_val is not None or s != freq_elem:
#                     new_stack.append(s)
#                 else:
#                     pop_val = s
#             self.stack = new_stack[::-1]
#             return pop_val


class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end
