# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        track = []
        use = [False for i in range(len(s))]

        def backtrack(track, s):
            if len(track) == len(s):
                res.append(''.join(track))
                return
            for i in range(len(s)):
                if use[i]:
                    continue
                use[i] = True
                track.append(s[i])
                backtrack(track, s)
                track.pop()
                use[i] = False
        backtrack(track, s)
        return list(set(res))
