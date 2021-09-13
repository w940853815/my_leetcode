#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# https://leetcode-cn.com/problems/number-of-boomerangs/description/
#
# algorithms
# Medium (60.36%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    40.8K
# Total Submissions: 62.5K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组
# ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
#
# 返回平面上所有回旋镖的数量。
#
#
# 示例 1：
#
#
# 输入：points = [[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#
#
# 示例 2：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：points = [[1,1]]
# 输出：0
#
#
#
#
# 提示：
#
#
# n == points.length
# 1
# points[i].length == 2
# -10^4 i, yi
# 所有点都 互不相同
#
#
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:

    # Time Limit Exceeded
    # def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    #     res = []
    #     track = []
    #     used = [False for _ in points]

    #     def backtrack(track):
    #         # print(track)
    #         if len(list(track)) == 3:
    #             i, j, k = track
    #             if (j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2 == (k[0] - i[0]) ** 2 + (
    #                 k[1] - i[1]
    #             ) ** 2:
    #                 res.append(list(track))
    #                 return
    #         for index, point in enumerate(points):
    #             if used[index]:
    #                 continue
    #             track.append(point)
    #             used[index] = True
    #             backtrack(track)
    #             track.pop()
    #             used[index] = False

    #     backtrack(track)
    #     return len(res)
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # 设 points 中有 m 个点到points[i] 的距离均相等，我们需要从这 mm 点中选出 2 个点当作回旋镖的 2 个端点，因此方案数即为在 m 个元素中选出 2 个不同元素的排列数
        ans = 0
        for p in points:
            res = defaultdict(int)
            for q in points:
                dis = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                res[dis] += 1
            for v in res.values():
                ans += v * (v - 1)
        return ans


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.numberOfBoomerangs(
        [[9, 3], [1, 9], [4, 7], [8, 4], [5, 0], [3, 6], [1, 0], [6, 3], [2, 0], [6, 1]]
    )
    print(res)
