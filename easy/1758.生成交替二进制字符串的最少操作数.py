#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        s_len = len(s)
        a = "".join(["01"[i % 2] for i in range(s_len)])
        b = "".join(["10"[i % 2] for i in range(s_len)])
        a_count, b_count = 0, 0
        for i, j in zip(a, s):
            if i != j:
                a_count += 1
        for i, j in zip(b, s):
            if i != j:
                b_count += 1
        return min(a_count, b_count)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.minOperations("0100")
    assert res == 1
