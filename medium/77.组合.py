#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        used = [False for i in range(n)]

        def backtrack(n, k):
            if len(track) == k:
                res.append(list(track))
                return
            for i in range(1, n + 1):
                if used[i - 1]:
                    continue
                if track and track[-1] >= i:
                    continue
                used[i - 1] = True
                track.append(i)
                backtrack(n, k)
                used[i - 1] = False
                track.pop()

        backtrack(n, k)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.combine(4, 2)
    print(res)
# @lc code=end
