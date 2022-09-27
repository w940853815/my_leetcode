#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from hashlib import new
from multiprocessing import reduction
from typing import List
from uuid import RESERVED_FUTURE

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        new_list = sorted(nums1)
        _len = len(new_list)
        if _len % 2:
            return new_list[_len // 2]
        else:
            return (new_list[_len // 2 - 1] + new_list[_len // 2]) / 2


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.findMedianSortedArrays([1, 3], [2])
    res = s.findMedianSortedArrays([1, 2], [3, 4])
    print(res)
