#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        same = defaultdict(int)
        for i, l1 in enumerate(list1):
            for j, l2 in enumerate(list2):
                if l1 == l2:
                    same[l1] = i + j
        min_sum = min(same.values())
        res = []
        for k, v in same.items():
            if v == min_sum:
                res.append(k)
        return res


# @lc code=end
