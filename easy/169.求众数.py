#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if res.get(num) == None:
                res[num] = 1
            else:
                res[num] += 1
        major_count = 0
        major_element = None
        for num, count in res.items():
            if count > major_count:
                major_count = count
                major_element = num
        return major_element
# @lc code=end
