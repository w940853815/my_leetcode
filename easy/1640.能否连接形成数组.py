#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#
from typing import List

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            if len(piece) == 1 and len(arr) == 1:
                return piece[0] in arr
            for i in range(1, len(piece)):
                try:
                    if arr.index(piece[i]) - arr.index(piece[i - 1]) != 1:
                        return False
                except:
                    # 元素不存在
                    return False
        return True


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # res = s.canFormArray([15, 88], [[88], [15]])
    # res = s.canFormArray([49, 18, 16], [[16, 18, 49]])
    # res = s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]])
    res = s.canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]])
    print(res)
