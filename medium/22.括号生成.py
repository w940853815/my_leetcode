#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = []

        def isValid(track):
            # 检查路径是否有效
            data = []
            for t in track:
                if t == '(':
                    data.append('(')
                else:
                    try:
                        data.pop()
                    except IndexError:
                        return False
            if data:
                return False
            else:
                return True

        def backtrack(track, n):
            if len(track) == n * 2:
                data = []
                # 第一个和最后一个分别不是()排除
                # '('个数和')'个数不等排除
                # 剩下情况检验括号是否匹配
                if track[0] == '(' and track[-1] == ')' and track.count('(') == track.count(')') and isValid(list(track)):
                    res.append(''.join(list(track)))
                return
            for i in['(', ')']:
                track.append(i)
                backtrack(track, n)
                track.pop()
        backtrack(track, n)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)
# @lc code=end
