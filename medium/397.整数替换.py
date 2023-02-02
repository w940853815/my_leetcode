#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 2 + min(
            self.integerReplacement((n + 1) // 2), self.integerReplacement((n - 1) // 2)
        )


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.integerReplacement(8)
    print(res)
    res = s.integerReplacement(4)
    print(res)
