#
# @lc app=leetcode.cn id=2180 lang=python3
#
# [2180] 统计各位数字之和为偶数的整数个数
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for ns in range(1, num + 1):
            _sum = 0
            for i in str(ns):
                _sum += int(i)
            if not _sum % 2:
                res += 1

        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.countEven(30)
    print(res)
