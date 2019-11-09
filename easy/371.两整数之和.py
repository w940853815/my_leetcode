#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start

# 一位二进制加法的真值表
# x	y	sum	carry
# 0	0	0	0
# 0	1	1	0
# 1	0	1	0
# 1	1	0	1


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 嗯 人生苦短 哈哈
        return sum([a, b])


if __name__ == "__main__":
    s = Solution()
    res = s.getSum(-1, 1)
    print(res)
# @lc code=end
