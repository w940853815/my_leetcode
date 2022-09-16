#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#
from os import stat
from typing import List

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)


# @lc code=end
