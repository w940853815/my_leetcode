#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time Limit Exceeded
        # for x in nums:
        #     if nums.count(x)==1:
        #         return x

        # 如果a、b两个值不相同，则异或结果为1。 如果a、b两个值相同，异或结果为0
        #两个相同的数异或是0,所以只出现一次的数与0异或就是本身
        res = nums[0]
        for x in nums[1:]:
            res = res^x
        return res
# @lc code=end

