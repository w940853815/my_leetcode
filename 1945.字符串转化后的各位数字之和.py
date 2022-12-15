#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        for i in range(k):
            _sum = 0
            for j in s:
                if ord(j) > 96:
                    new_s = str(ord(j) - 96)
                else:
                    new_s = str(j)
                for z in new_s:
                    _sum += int(z)
            s = str(_sum)
        return int(s)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.getLucky("leetcode", 2)
    assert 6 == res
