#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.78%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    109.7K
# Total Submissions: 244.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
#
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#
#
# 进阶：
#
#
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#
#
from typing import List
# @lc code=start


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums)
        flag = False
        if not nums:
            return 0
        while r < len(nums):
            r += 1
            while(sum(nums[l:r]) >= s):
                # print(nums[l:r], sum(nums[l:r]), s)
                # print(min(len(nums[l:r]), res), len(nums[l:r]), res)
                res = min(len(nums[l:r]), res)
                l += 1
                flag = True
        return res if flag else 0


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # res = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    # 15 [5,1,3,5,10,7,4,9,2,8]
    res = s.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8])
    print(res)
