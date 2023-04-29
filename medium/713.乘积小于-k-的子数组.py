#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
# https://leetcode.cn/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (49.42%)
# Likes:    682
# Dislikes: 0
# Total Accepted:    99.7K
# Total Submissions: 201.7K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#
#
# 示例 1：
#
#
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3], k = 0
# 输出：0
#
#
#
# 提示: 
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#
from typing import List
# @lc code=start


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded
        # 35/97 cases passed (N/A)
        # pre_prod = [1]
        # n = len(nums)
        # ans = []
        # for i in range(n):
        #     pre_prod.append(pre_prod[i]*nums[i])
        # for i in range(n):
        #     for j in range(i, n):
        #         if pre_prod[j+1]//pre_prod[i] < k:
        #             ans.append(nums[i:j+1])
        # return len(ans)
        ans,j,prod=0,0,1
        for i,num in enumerate(nums):
            prod*=num
            while j<=i and prod>=k:
                prod//=nums[j]
                j+=1
            ans=ans+i-j+1
        return ans

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(res)
    res = s.numSubarrayProductLessThanK([1, 2, 3], 0)
    print(res)

