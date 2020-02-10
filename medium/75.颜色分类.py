#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for n in nums:
            if n == 0:
                count[0] += 1
            elif n == 1:
                count[1] += 1
            else:
                count[2] += 1
        n = 0
        for key, value in count.items():
            for i in range(value):
                nums[n] = key
                n += 1


# @lc code=end
