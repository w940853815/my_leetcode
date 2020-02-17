#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                r = bin(i) + bin(j)
                if r.count('1') == num:
                    res.append("{:d}:{:0>2d}".format(i, j))
        return res


# @lc code=end
