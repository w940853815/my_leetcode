#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
# https://leetcode-cn.com/problems/contiguous-array/description/
#
# algorithms
# Medium (45.83%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    32.5K
# Total Submissions: 62.4K
# Testcase Example:  '[0,1]'
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#
#
# 示例 1:
#
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
#
# 示例 2:
#
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
#
#
#
# 提示：
#
#
# 1
# nums[i] 不是 0 就是 1
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        count = 0
        ans = 0
        for index, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in map:
                prefix = map.get(count)
                ans = max(index - prefix, ans)
            else:
                map[count] = index
        return ans


# @lc code=end
