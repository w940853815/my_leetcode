#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (40.03%)
# Likes:    276
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 47.1K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
#
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
# 示例 2：
#
#
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
# -10^5
#
#
#
#
# 进阶：如果行数远大于列数，该如何设计解决方案？
#
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList

        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans


# @lc code=end
