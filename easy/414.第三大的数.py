#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (35.02%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    32.1K
# Total Submissions: 90.9K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
#
# 示例 1:
#
#
# 输入: [3, 2, 1]
#
# 输出: 1
#
# 解释: 第三大的数是 1.
#
#
# 示例 2:
#
#
# 输入: [1, 2]
#
# 输出: 2
#
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
#
#
# 示例 3:
#
#
# 输入: [2, 2, 3, 1]
#
# 输出: 1
#
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
#
#
#

# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]

# @lc code=end
