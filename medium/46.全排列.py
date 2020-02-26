#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start

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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        def backtrack(track, nums):
            if len(track) == len(nums):
                # 列表深拷贝
                tmp = list(track)
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(track, nums)
                track.pop()

        backtrack(track, nums)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)
# @lc code=end
