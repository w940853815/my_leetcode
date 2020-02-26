#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from typing import List
"""
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        used = [False for i in nums]
        def backtrack(track, nums):

            if len(track) == len(nums):
                res.append(list(track))
                return
            for i in range(len(nums)):
                ####### 关键两个剪枝条件start #######
                if used[i]:
                    continue
                if i > 0 and nums[i - 1] == nums[i] and used[i - 1]:
                    continue
                ####### 关键两个剪枝条件end #######
                used[i] = True
                track.append(nums[i])
                backtrack(track, nums)
                used[i] = False
                track.pop()
        backtrack([], nums)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.permuteUnique([1, 1, 2])
    print(res)
    print(len(res))
# @lc code=end
