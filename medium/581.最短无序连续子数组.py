#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (36.96%)
# Likes:    644
# Dislikes: 0
# Total Accepted:    82.6K
# Total Submissions: 209.8K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3,4]
# 输出：0
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1
# -10^5
#
#
#
#
# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
#
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_list = sorted(nums)
        start = end = -1
        print(nums, sort_list)
        for index, num in enumerate(nums):
            if num != sort_list[index]:
                if start == -1:
                    start = index
                else:
                    end = index
        print(end, start)
        if end - start:
            return end - start + 1
        else:
            return 0


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    len = s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    print(len)