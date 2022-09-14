#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#
from copy import deepcopy

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        _max = 0
        num_arry = [i for i in str(num)]
        _len = len(num_arry)
        for i in range(_len):
            for j in range(_len):
                tmp = deepcopy(num_arry)
                tmp[i], tmp[j] = tmp[j], tmp[i]
                _max = max(int("".join(tmp)), _max)
        return _max


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.maximumSwap(2736)
    print(res)
    res = s.maximumSwap(98368)
    print(res)
    res = s.maximumSwap(9973)
    print(res)
