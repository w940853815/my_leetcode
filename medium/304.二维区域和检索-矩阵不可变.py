#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode.cn/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (61.36%)
# Likes:    488
# Dislikes: 0
# Total Accepted:    122.8K
# Total Submissions: 200.1K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +'[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵 matrix，以下类型的多个请求：
#
#
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
#
#
# 实现 NumMatrix 类：
#
#
# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1)
# 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。
#
#
#
#
# 示例 1：
#
#
#
#
# 输入:
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
#
# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
# 输出:
# [null, 8, 11, 12]
#
# 解释:
# NumMatrix numMatrix = new
# NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^5 <= matrix[i][j] <= 10^5
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# 最多调用 10^4 次 sumRegion 方法
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


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

if __name__ == '__main__':
    nm = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
                   1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(nm.sumRegion(0, 0, 2, 2))
    print(nm.sumRegion(2, 1, 4, 3))
