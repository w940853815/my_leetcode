#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
# https://leetcode.cn/problems/super-ugly-number/description/
#
# algorithms
# Medium (57.06%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    57.8K
# Total Submissions: 101.4K
# Testcase Example:  '12\n[2,7,13,19]'
#
# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
#
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
#
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
#
#
#
# 示例 1：
#
#
# 输入：n = 12, primes = [2,7,13,19]
# 输出：32
# 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12
# 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
#
# 示例 2：
#
#
# 输入：n = 1, primes = [2,3,5]
# 输出：1
# 解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
#
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# 1 <= primes.length <= 100
# 2 <= primes[i] <= 1000
# 题目数据 保证 primes[i] 是一个质数
# primes 中的所有值都 互不相同 ，且按 递增顺序 排列
#
#
#
#
#
#
from typing import List
import heapq
# @lc code=start


class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = []
        hq = [1]
        heapq.heapify(hq)
        for i in range(n):
            cur = heapq.heappop(hq)
            for prime in primes:
                tmp = cur*prime
                if tmp not in seen:
                    seen.append(tmp)
                    heapq.heappush(hq, tmp)
        return cur


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.nthSuperUglyNumber(12, [2, 7, 13, 19])
    print(res)
    res = s.nthSuperUglyNumber(1, [2, 3, 5])
    print(res)
    # Time Limit Exceeded
    # 81/87 cases passed (N/A)
    res = s.nthSuperUglyNumber(100000, [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103,
                               109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251])
    print(res)  # 1092889481
