#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (41.06%)
# Likes:    399
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 278.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
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
# -10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for _list in matrix:
            res.extend(_list)
        left = 0
        right = len(res) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > res[mid]:
                left = mid + 1
            if target < res[mid]:
                right = mid - 1
            if target == res[mid]:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.searchMatrix([[1]], 2)
    print(res)