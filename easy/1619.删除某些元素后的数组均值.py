#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#
from typing import List

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        remove_count = int(len(arr) * 0.05)
        for i in range(remove_count):
            arr.remove(min(arr))
            arr.remove(max(arr))
        return sum(arr) / len(arr)


# @lc code=end
