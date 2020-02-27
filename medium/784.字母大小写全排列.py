#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
from typing import List
"""
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""
# @lc code=start


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        track = []
        array = list(S)

        def backtrack(track, index, array):
            if len(S) == len(track):
                res.append(''.join(list(track)))
                return
            if S[index].isdigit():
                track.append(array[index])
                backtrack(track, index + 1, array)
                track.pop()
            else:
                track.append(array[index])
                backtrack(track, index + 1, array)
                track.pop()
                array[index] = chr(ord(array[index]) ^ (1 << 5))
                track.append(array[index])
                backtrack(track, index + 1, array)
                track.pop()

        backtrack([], 0, array)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.letterCasePermutation('a1b2')
    print(res)
# @lc code=end
