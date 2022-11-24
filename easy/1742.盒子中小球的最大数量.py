#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#
from collections import defaultdict

# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball_dict = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            _sum = sum([int(n) for n in str(i)])
            ball_dict[_sum] += 1
        return max(ball_dict.values())


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.countBalls(1, 10)
    assert res == 2
