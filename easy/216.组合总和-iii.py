#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (71.35%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    37.4K
# Total Submissions: 51.1K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

# @lc code=start


from typing import List

from numpy.ma.core import sort


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        track = []

        def backtrack(start, track):
            if len(track) == k:
                if sum(track) == n and len(set(track)) == len(track):
                    res.append(list(track))
                return
            for i in range(start, 10):
                track.append(i)
                backtrack(i, track)
                track.pop()
        backtrack(1, track)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum3(8, 36)
    print(res)
# @lc code=end
