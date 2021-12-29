#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#
# https://leetcode-cn.com/problems/count-special-quadruplets/description/
#
# algorithms
# Easy (56.36%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 39.7K
# Testcase Example:  '[1,2,3,6]'
#
# 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
#
#
# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d
#
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,6]
# 输出：1
# 解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
#
#
# 示例 2：
#
# 输入：nums = [3,3,6,4,5]
# 输出：0
# 解释：[3,3,6,4,5] 中不存在满足要求的四元组。
#
#
# 示例 3：
#
# 输入：nums = [1,1,1,3,5]
# 输出：4
# 解释：满足要求的 4 个四元组如下：
# - (0, 1, 2, 3): 1 + 1 + 1 == 3
# - (0, 1, 3, 4): 1 + 1 + 3 == 5
# - (0, 2, 3, 4): 1 + 1 + 3 == 5
# - (1, 2, 3, 4): 1 + 1 + 3 == 5
#
#
#
#
# 提示：
#
#
# 4 <= nums.length <= 50
# 1 <= nums[i] <= 100
#
#
#
from typing import List

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for ai, a in enumerate(nums):
            for bi, b in enumerate(nums[ai + 1 :]):
                for ci, c in enumerate(nums[ai + bi + 2 :]):
                    for di, d in enumerate(nums[ai + bi + ci + 3 :]):
                        if a + b + c == d:
                            count += 1
        return count


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.countQuadruplets([1, 2, 3, 6])
    print(res)
