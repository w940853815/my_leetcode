#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.57%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    105.3K
# Total Submissions: 176.7K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quick_sort(nums):
            if len(nums) < 2:
                return nums
            poivt = nums[0]
            less_lists = [i for i in nums if i < poivt]
            medium = [i for i in nums if i == poivt]
            greater_lists = [i for i in nums if i > poivt]
            return quick_sort(less_lists)+medium+quick_sort(greater_lists)
        return quick_sort(nums)


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.sortArray([1, 6, 3, 1, 4, 5])
    print(res)
