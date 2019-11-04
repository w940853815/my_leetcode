#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        mid = length // 2 + 1 if length % 2 == 1 else length // 2
        for x in range(mid):
            tmp = s[-x - 1]
            s[-x - 1] = s[x]
            s[x] = tmp


# @lc code=end
