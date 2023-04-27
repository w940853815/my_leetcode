#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.39%)
# Likes:    1481
# Dislikes: 0
# Total Accepted:    285.8K
# Total Submissions: 389.4K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#
from typing import List
# @lc code=start


class Solution:
    def __init__(self) -> None:
        self.traceker = []
        self.res = []

    def valid_str(self, s: str):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtracke(self, s, start):
        if start == len(s):
            self.res.append(self.traceker[:])
            return
        for i in range(start, len(s)):
            if not self.valid_str(s[start:i+1]):
                continue
            self.traceker.append(s[start:i+1])
            self.backtracke(s, i+1)
            self.traceker.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backtracke(s, 0)
        return self.res


# @lc code=end
