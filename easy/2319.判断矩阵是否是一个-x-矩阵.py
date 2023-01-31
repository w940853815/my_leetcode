#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#
from typing import List

# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid[0])
        x_index = set()
        for i in range(n):
            x_index.add((i + 1) * (n - 1))
            x_index.add(i * (n + 1))
        index = 0
        for (i, data_x) in enumerate(grid):
            for _, data_y in enumerate(data_x):
                if index in x_index:
                    if data_y == 0:
                        return False
                else:
                    if data_y != 0:
                        return False
                index += 1
        return True


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
    print(res)
