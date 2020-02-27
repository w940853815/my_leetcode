#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List
"""
第一次没有看题解自己使用回溯法解出来
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        track = []
        array = []
        if len(digits) == 0:
            return []
        key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for d in digits:
            array.append(key_map[d])

        def backtrack(track, array, index):
            if len(track) == len(digits):
                res.append(''.join(track))
                return
            for i in range(len(array[index])):
                track.append(array[index][i])
                backtrack(track, array, index + 1)
                track.pop()
        backtrack(track, array, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.letterCombinations('23')
    print(res)
# @lc code=end
