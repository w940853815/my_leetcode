#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#
from typing import List

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in range(len(gain)):
            res.append(res[i] + gain[i])
        return max(res)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.largestAltitude([-5, 1, 5, 0, -7])
    print(res)
    assert res == 1
    res = s.largestAltitude([52, -91, 72])
    print(res)
    assert res == 52
