#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op == "++X" or op == "X++":
                x += 1
            else:
                x -= 1
        return x


# @lc code=end
