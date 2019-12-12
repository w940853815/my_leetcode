#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n != 0:
            n -= 1
            res = res + chr(n % 26 + 65)
            n = int(n / 26)
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    res = s.convertToTitle(26)
    print(res)
    res = s.convertToTitle(52)
    print(res)
    res = s.convertToTitle(28)
    print(res)
    res = s.convertToTitle(701)
    print(res)
# @lc code=end
