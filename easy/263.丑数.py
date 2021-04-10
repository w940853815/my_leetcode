#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
# https://leetcode-cn.com/problems/ugly-number/description/
#
# algorithms
# Easy (50.07%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    69.1K
# Total Submissions: 135.8K
# Testcase Example:  '6'
#
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
#
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
# 示例 1：
#
#
# 输入：n = 6
# 输出：true
# 解释：6 = 2 × 3
#
# 示例 2：
#
#
# 输入：n = 8
# 输出：true
# 解释：8 = 2 × 2 × 2
#
#
# 示例 3：
#
#
# 输入：n = 14
# 输出：false
# 解释：14 不是丑数，因为它包含了另外一个质因数 7 。
#
#
# 示例 4：
#
#
# 输入：n = 1
# 输出：true
# 解释：1 通常被视为丑数。
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        primes = [2, 3, 5]
        for prime in primes:
            while n % prime == 0:
                n = n // prime
        return n == 1


# @lc code=end
