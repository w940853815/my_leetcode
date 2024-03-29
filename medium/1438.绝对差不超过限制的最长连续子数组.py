#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (49.49%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 90.2K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
#
# 如果不存在满足条件的子数组，则返回 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
#
#
# 示例 2：
#
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#
#
# 示例 3：
#
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
#
#
#
from typing import List
# @lc code=start
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Time Limit Exceeded
        # 56/61 cases passed (N/A)
        # left, right = 0, 0
        # window = []
        # res = 0
        # while right < len(nums):
        #     c = nums[right]
        #     window.append(c)
        #     while max(window)-min(window) > limit:
        #         d = nums[left]
        #         left += 1
        #         window.remove(d)
        #     res = max(res, right-left+1)
        #     right += 1
        # return res
        left, right = 0, 0
        window = SortedList()
        res = 0
        while right < len(nums):
            c = nums[right]
            window.add(c)
            while window[-1]-window[0] > limit:
                d = nums[left]
                left += 1
                window.remove(d)
            res = max(res, right-left+1)
            right += 1
        return res


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.longestSubarray([8, 2, 4, 7], 4)
    print(res)
    res = s.longestSubarray([10, 1, 2, 4, 7, 2], 5)
    print(res)
    res = s.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0)
    print(res)
