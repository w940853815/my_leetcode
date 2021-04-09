#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (50.56%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    86.3K
# Total Submissions: 163.7K
# Testcase Example:  '[1,3,5]'
#
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7]
# 在变化后可能得到：
#
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
#
#
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,5]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,2,0,1]
# 输出：0
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1
# -5000
# nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#
#
#
# 进阶：
#
#
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#
#
from typing import List

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        left = 0
        right = len(nums) - 1
        # while left < right:
        #     mid = (right + left) // 2
        #     if nums[right] < nums[mid]:
        #         left = mid + 1
        #     elif nums[right] > nums[mid]:
        #         right = mid
        #     else:
        #         right -= 1

        while left < right:
            mid = (right + left) // 2
            if nums[right] == nums[mid]:
                right -= 1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.findMin([1, 3, 5])
    print(res)
    res = s.findMin([3, 1])
    print(res)
    res = s.findMin([2, 2, 2, 0, 1])
    print(res)
