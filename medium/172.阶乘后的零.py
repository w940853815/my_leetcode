#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res *= i
        c = 0
        for j in str(res)[::-1]:
            if j != "0":
                break
            c += 1
        return c


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.trailingZeroes(5)
    assert 1 == res
    res = s.trailingZeroes(0)
    assert 0 == res
    res = s.trailingZeroes(3)
    assert 0 == res
