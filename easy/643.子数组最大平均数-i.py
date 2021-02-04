#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (39.68%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 67.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
#
#
# 示例：
#
#
# 输入：[1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 提示：
#
#
# 1 k n
# 所给数据范围 [-10,000，10,000]。
#
#
#
from typing import List
# @lc code=start


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 滑动窗口
        left = 0
        right = k-1
        max_sum = window = sum(nums[left:right+1])
        while right < len(nums)-1:
            window -= nums[left]
            left += 1
            right += 1
            window += nums[right]
            # print(left, right, window)

            if max_sum < window:
                max_sum = window

        return max_sum/k


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.findMaxAverage([0, 1, 1, 3, 3], 4)
    print(res)
