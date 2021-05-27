#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (79.07%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    141.5K
# Total Submissions: 175.3K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 2^31.
#
# 示例:
#
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
#
#
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp = x ^ y
        res = 0
        for i in range(32):
            if tmp & 1 == 1:
                res += 1
            tmp = tmp >> 1

        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.hammingDistance(93, 73)
    print(res)
