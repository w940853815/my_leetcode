#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#
from multiprocessing import reduction
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums).most_common()
        count = sorted(count, key=lambda x: (x[1], -x[0]))
        res = []
        for c in count:
            for x in range(c[1]):
                res.append(c[0])
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1])
    print(res)
