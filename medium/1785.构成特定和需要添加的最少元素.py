#
# @lc app=leetcode.cn id=1785 lang=python3
#
# [1785] 构成特定和需要添加的最少元素
#
from typing import List

# @lc code=start
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums) - goal) + limit - 1) // limit


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # res = s.minElements([1, -1, 1], 3, -4)
    # assert res == 2
    res = s.minElements([1, -10, 9, 1], 100, 0)
    assert res == 1
