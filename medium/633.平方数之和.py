#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (35.20%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    73.9K
# Total Submissions: 188.2K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。
#
#
#
# 示例 1：
#
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#
#
# 示例 2：
#
# 输入：c = 3
# 输出：false
#
#
# 示例 3：
#
# 输入：c = 4
# 输出：true
#
#
# 示例 4：
#
# 输入：c = 2
# 输出：true
#
#
# 示例 5：
#
# 输入：c = 1
# 输出：true
#
#
#
# 提示：
#
#
# 0 <= c <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math

        low = 0
        high = int(math.sqrt(c))
        while low <= high:
            if low * low + high * high < c:
                low += 1
            elif low * low + high * high > c:
                high -= 1
            else:
                # print(low, high)
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(3))