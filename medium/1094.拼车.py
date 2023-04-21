#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
# https://leetcode.cn/problems/car-pooling/description/
#
# algorithms
# Medium (52.10%)
# Likes:    241
# Dislikes: 0
# Total Accepted:    70.9K
# Total Submissions: 136.1K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
#
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
#
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i
# 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
#
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
#
#
# 示例 1：
#
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
#
#
# 示例 2：
#
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 10^5
#
#
#
from typing import List
# @lc code=start


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for i in range(1000)]
        res = [0 for i in range(1000)]
        for trip in trips:
            val = trip[0]
            from_i = trip[1]
            to_j = trip[2]
            diff[from_i] += val
            if to_j < 1000:
                diff[to_j] -= val
        for i in range(1000):
            res[i] = diff[i]+res[i-1]
        return max(res) <= capacity


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.carPooling([[2, 1, 5], [3, 3, 7]], 4)
    print(res)
    res = s.carPooling([[2, 1, 5], [3, 3, 7]], 5)
    print(res)
    res = s.carPooling([[2, 1, 5], [3, 5, 7]], 3)  # expect true
    print(res)
