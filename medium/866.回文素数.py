#
# @lc app=leetcode.cn id=866 lang=python3
#
# [866] 回文素数
#

# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            return n > 1 and all([x % i for i in range(2, int(x**0.5 + 1))])

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        while True:
            if reverse(n) == n and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.primePalindrome(13)
    print(res)
