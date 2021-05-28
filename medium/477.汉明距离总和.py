#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#
# https://leetcode-cn.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (53.26%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    31.2K
# Total Submissions: 52.9K
# Testcase Example:  '[4,14,2]'
#
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 计算一个数组中，任意两个数之间汉明距离的总和。
#
# 示例:
#
#
# 输入: 4, 14, 2
#
# 输出: 6
#
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
#
#
# 注意:
#
#
# 数组中元素的范围为从 0到 10^9。
# 数组的长度不超过 10^4。
#
#
#
from typing import List

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(30):
            c = 0
            for num in nums:
                num = num >> i
                if num & 1 == 1:
                    c += 1
            res = res + c * (n - c)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.totalHammingDistance([4, 14, 2])
    print(res)