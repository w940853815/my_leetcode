#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (30.15%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 41.1K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
# 说明:
#
#
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
# 示例 1:
#
#
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 状态：超出时间限制

        # res = 0

        # def find_min_dist(hoursen):
        #     # 某个屋子距每个加热器的最小距离
        #     radius = float("inf")
        #     for heater in heaters:
        #         radius = min(radius, abs(heater-hourse))
        #     return radius

        # for hourse in houses:
        #     res = max(res, find_min_dist(hourse))
        # return res
        # @lc code=end
        result = []
        # 特殊情况，只有一个加热器。
        if len(heaters) == 1:
            for item in houses:
                result.append(abs(item-heaters[0]))
            return max(result)

        houses.sort()  # 进行排序。
        heaters.sort()
        pin1 = 0  # 指向房屋的前一个加热器
        pin2 = 1  # 指向房屋的后一个加热器

        for house in houses:
            while pin2 < len(heaters)-1 and heaters[pin2] < house:
                pin2 += 1
                pin1 += 1
            # 取房屋与前后加热器的最小距离
            result.append(
                min(abs(house-heaters[pin1]), abs(heaters[pin2]-house)))

        return max(result)  # 返回结果最大值


if __name__ == "__main__":
    s = Solution()
    res = s.findRadius([1, 2, 3, 4], [1, 4])
    print(res)
