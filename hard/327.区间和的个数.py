#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# https://leetcode.cn/problems/count-of-range-sum/description/
#
# algorithms
# Hard (40.96%)
# Likes:    537
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 98K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
#
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
#
# 示例 1：
#
#
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
#
#
# 示例 2：
#
#
# 输入：nums = [0], lower = 0, upper = 0
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# -2^31
# -10^5
# 题目数据保证答案是一个 32 位 的整数
#
#
#
from typing import List
# @lc code=start


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Time Limit Exceeded
        # 59/67 cases passed (N/A)
        pre_sum = [0]
        count = 0
        n = len(nums)
        for i in range(n):
            pre_sum.append(pre_sum[i]+nums[i])
        for i in range(n):
            for j in range(i, n):
                sum_ij = pre_sum[j+1]-pre_sum[i]
                if sum_ij >= lower and sum_ij <= upper:
                    # print(i, j, sum_ij)
                    count += 1
        return count


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.countRangeSum([-2, 5, -1], -2, 2)
    print(res)
    res = s.countRangeSum([0], 0, 0)
    print(res)
