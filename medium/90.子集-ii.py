#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.92%)
# Likes:    535
# Dislikes: 0
# Total Accepted:    96K
# Total Submissions: 152K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1
# -10
#
#
#
#
#
from typing import List

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            res.append(list(track))
            for index in range(i, len(nums)):
                if index > i and nums[index] == nums[index - 1]:
                    continue
                track.append(nums[index])
                backtrack(index + 1)
                track.pop()

        res = []
        track = []
        nums.sort()
        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.subsetsWithDup([1, 2, 2])
    print(res)
