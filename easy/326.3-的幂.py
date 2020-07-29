#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        while True:
            print(x)
            if 3 ** x < n:
                x = x+1
            if 3 ** x == n:
                return True
            if 3 ** x > n:
                return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(9))
# @lc code=end
