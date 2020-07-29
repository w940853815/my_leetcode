#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        _map = {}
        for i, index in enumerate(indices):
            _map[index] = s[i]
        res = ''
        for i in range(len(indices)):
            res += _map[i]
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.restoreString("codeleet",
                          [4, 5, 6, 7, 0, 2, 1, 3])
    print(res)
