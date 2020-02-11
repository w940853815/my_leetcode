#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List


class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 按照上，右，下，左的顺序搜索

        x_max = len(board)
        y_max = len(board[0])
        mark = [[False for _ in range(y_max)] for _ in range(x_max)]
        for i in range(x_max):
            for j in range(y_max):
                if self.search_word(board, word, mark, 0, i, j, x_max, y_max):
                    return True
        return False

    def search_word(self, board, word, mark, index, start_x, start_y, x_max, y_max):
        # 终止递归条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if word[index] == board[start_x][start_y]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            mark[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < x_max and 0 <= new_y < y_max and not mark[new_x][new_y] and self.search_word(board, word, mark, index + 1, new_x, new_y, x_max, y_max):
                    return True

            mark[start_x][start_y] = False
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "ABCCED"))

# @lc code=end
