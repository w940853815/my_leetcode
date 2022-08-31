#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from os import stat
from typing import List

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for push in pushed:
            stack.append(push)
            while len(stack) > 0 and popped[i] == stack[-1]:
                stack.pop()
                i = i + 1
        return len(stack) == 0


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    print(res)
    res = s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
    print(res)
