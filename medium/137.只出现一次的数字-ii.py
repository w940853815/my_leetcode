#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (68.70%)
# Likes:    643
# Dislikes: 0
# Total Accepted:    81.1K
# Total Submissions: 113.6K
# Testcase Example:  '[2,2,3,2]'
#
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,2,3,2]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#
#
#
#
# 提示：
#
#
# 1
# -2^31
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
#
#
#
#
# 进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#
from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1

        for key, val in res.items():
            if val == 1:
                return key


# @lc code=end
