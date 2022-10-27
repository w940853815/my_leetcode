#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#
from typing import List

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        neg_count = 0
        for i in nums:
            if i < 0:
                neg_count += 1
        if neg_count % 2:
            return -1
        else:
            return 1


if __name__ == "__main__":
    s = Solution()
    res = s.arraySign([-1, -2, -3, -4, 3, 2, 1])
    print(res)

# @lc code=end
