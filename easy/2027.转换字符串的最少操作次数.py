#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        covered = -1
        res = 0
        for i, x in enumerate(s):
            if x == "X" and i > covered:
                res += 1
                covered = i + 2
        return res


# @lc code=end
