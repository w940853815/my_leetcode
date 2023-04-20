#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#
# https://leetcode.cn/problems/matrix-block-sum/description/
#
# algorithms
# Medium (75.64%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 30.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素
# mat[r][c] 的和： 
#
#
# i - k
# j - k  且
# (r, c) 在矩阵内。
#
#
#
#
# 示例 1：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#
#
# 示例 2：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#
#
#
#
# 提示：
#
#
# m == mat.length
# n == mat[i].length
# 1
# 1
#
#
#
from typing import List

# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = [[0 for _ in range(len(matrix[0])+1)]
                        for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.pre_sum[i+1][j+1] = matrix[i][j] + self.pre_sum[i][j+1] + \
                    self.pre_sum[i+1][j]-self.pre_sum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2+1][col2+1]-self.pre_sum[row2+1][col1]-self.pre_sum[row1][col2+1]+self.pre_sum[row1][col1]


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        numMatrix = NumMatrix(mat)
        m, n = len(mat), len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = max(i-k, 0), max(j-k, 0)
                x2, y2 = min(i+k, m-1), min(j+k, n-1)
                res[i][j] = numMatrix.sumRegion(x1, y1, x2, y2)
        return res


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    print(res)
    res = s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
    print(res)
