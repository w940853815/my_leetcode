# https://leetcode-cn.com/problems/volume-of-histogram-lcci/
# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0

        while left < right:
            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            if height[left] >= height[right]:
                res += right_max - height[right]
                right -= 1
        return res