#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (40.11%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 66.7K
# Testcase Example:  '[1,2,3]'
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
#
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
#
#
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#
#
#
#
# 提示：
#
#
# 1
# 1
# nums 中的所有整数 互不相同
#
#
#
from typing import List

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        if n == 1:
            return nums
        dp = [[x] for x in nums]
        max_res = []
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and (len(dp[j]) + 1) > len(dp[i]):
                    dp[i] = dp[j] + nums[i : i + 1]

            if len(dp[i]) > len(max_res):
                max_res = dp[i]
        return max_res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.largestDivisibleSubset([1, 2, 4, 8])
    print(res)