#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.09%)
# Total Accepted:    49.3K
# Total Submissions: 111.9K
# Testcase Example:  'sum_tmp'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums) -> int:
        def find_max_subArray(low,high,A):
            mid = int((low + high) / 2)
            if high==low:
                return low,high,A[low] #只有一个元素
            else:
                left_low,left_high,left_sum=find_max_subArray(low,mid,A)
                print('left',left_low,left_high,left_sum)
                right_low,right_high,right_sum=find_max_subArray(mid+1,high,A)
                print('right',right_low,right_high,right_sum)
                cross_low,cross_high,cross_sum = find_max_cross_subArray(low,mid,high,A)
                print('cross',cross_low,cross_high,cross_sum)
                if left_sum>=right_sum and left_sum>=cross_sum:
                    return left_low,left_high,left_sum
                if right_sum>=left_sum and right_sum>=cross_sum:
                    return right_low,right_high,right_sum
                else:
                    return cross_low,cross_high,cross_sum

        def find_max_cross_subArray(low,mid,high,A):
            print(11111,low,mid,high,A)

            sum=0
            max_left=None
            max_right=None
            left_sum=float('-inf')
            for i in range(mid,low,-1):
                sum = sum+A[i]
                if sum > left_sum:
                    left_sum = sum
                    max_left = i
            right_sum = float('-inf')
            sum = 0
            for i in range(mid+1,high):
                sum = sum+A[i]
                if sum > right_sum:
                    right_sum = sum
                    max_right = i
            return max_left,max_right,left_sum+right_sum

        c, b, max = find_max_subArray(0, len(nums)-1, nums)
        print(c,b,max)
        return max


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s=Solution()
    a=s.maxSubArray(nums)
    print(a)
    