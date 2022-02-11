#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#
# https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
#
# algorithms
# Easy (57.94%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 46.4K
# Testcase Example:  '[90]\n1'
#
# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
#
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
#
# 返回可能的 最小差值 。
#
#
#
# 示例 1：
#
# 输入：nums = [90], k = 1
# 输出：0
# 解释：选出 1 名学生的分数，仅有 1 种方法：
# - [90] 最高分和最低分之间的差值是 90 - 90 = 0
# 可能的最小差值是 0
#
#
# 示例 2：
#
# 输入：nums = [9,4,1,7], k = 2
# 输出：2
# 解释：选出 2 名学生的分数，有 6 种方法：
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
# - [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
# - [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
# - [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
# 可能的最小差值是 2
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 10^5
#
#
#
from typing import List
from itertools import combinations

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded
        # if k < 2:
        #     return 0
        # else:
        #     res = float("inf")
        #     for c in combinations(nums, k):
        #         res = min(res, max(c) - min(c))
        #     return res
        if k < 2:
            return 0
        else:
            res = float("inf")
            nums.sort()
            _len = len(nums)
            for i in range(_len - k + 1):
                res = min(res, nums[i + k - 1] - nums[i])
            return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6)
    print(res)
    res = s.minimumDifference(
        [
            1730,
            78090,
            78197,
            76063,
            41072,
            25772,
            64973,
            44059,
            97954,
            20449,
            37462,
            60265,
            53283,
            43481,
            81501,
            73746,
            19123,
            34867,
            12144,
            62845,
            77983,
            59895,
            57157,
            38916,
            56188,
            37623,
            52200,
            88411,
            30711,
            28715,
            51323,
            77016,
            30741,
            63977,
            3071,
            9129,
            20313,
            80290,
            11220,
            90641,
            8553,
            79604,
            46684,
            86482,
            85661,
            55637,
            5453,
            86799,
            56086,
            80546,
            70214,
            99889,
            8780,
            48720,
            11455,
            47179,
            52401,
            44928,
            16540,
            65339,
            41927,
        ],
        52,
    )
    print(res)
