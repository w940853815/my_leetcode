#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (55.47%)
# Likes:    541
# Dislikes: 0
# Total Accepted:    56K
# Total Submissions: 99.6K
# Testcase Example:  '10'
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
# 示例 1：
#
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
#
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq

        res = []
        heapq.heappush(res, 1)
        seen = [1]
        primes = [2, 3, 5]
        for i in range(n):
            # print(res)
            cur = heapq.heappop(res)
            for prime in primes:
                tmp = prime * cur
                if tmp not in seen:
                    seen.append(tmp)
                    heapq.heappush(res, tmp)
        return cur


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.nthUglyNumber(10)
    print(res)
