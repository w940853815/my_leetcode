#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (26.44%)
# Likes:    659
# Dislikes: 0
# Total Accepted:    47.1K
# Total Submissions: 178.1K
# Testcase Example:  '[1]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回
# -1 。
#
# 子数组 是数组中 连续 的一部分。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1], k = 1
# 输出：1
#
#
# 示例 2：
#
#
# 输入：nums = [1,2], k = 4
# 输出：-1
#
#
# 示例 3：
#
#
# 输入：nums = [2,-1,2], k = 3
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9
#
#
#
from typing import List
# @lc code=start


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded
        # 82/97 cases passed (N/A)
        pre_sum = [0]
        res = float('inf')
        n = len(nums)
        for i in range(n):
            pre_sum.append(pre_sum[i]+nums[i])
        # print(pre_sum)
        for i in range(n):
            for j in range(i, n):
                sum_ij = pre_sum[j+1]-pre_sum[i]
                if sum_ij >= k:
                    # print(i, j, sum_ij)
                    res = min(res, j-i+1)
        if isinstance(res, float):
            return -1
        else:
            return res


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.shortestSubarray([1], 1)
    print(res)
    res = s.shortestSubarray([1, 2], 4)
    print(res)
    res = s.shortestSubarray([2, -1, 2], 3)
    print(res)
