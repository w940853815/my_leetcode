#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#
from typing import List
# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2)| set(nums1)&set(nums3)| set(nums2)&set(nums3))
# @lc code=end

if __name__=='__main__':
    s=Solution()
    res=s.twoOutOfThree([1,1,3,2],[2,3],[3])
    print(res)