#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (25.99%)
# Likes:    786
# Dislikes: 0
# Total Accepted:    118.7K
# Total Submissions: 417.8K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
#
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
#
#
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。
#
#
#
# 示例 1：
#
#
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
# 示例 2：
#
#
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#
# 示例 3：
#
#
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#
#
# 示例 4：
#
#
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。
#
#
#
# 提示：
#
#
# 1
# s 只包含数字，并且可能包含前导零。
#
#
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        dp = [0] * (len(s))
        legalset = set(str(i) for i in range(1, 27))
        dp[0] = 1
        if s[1] not in legalset:
            # s[1]='0'
            # 10,20,30
            # s[i]自身不能解码，只有一种情况
            dp[1] = 1 if s[:2] in legalset else 0

        else:
            dp[1] = 2 if s[:2] in legalset else 1
        for i in range(2, len(s)):
            if s[i] not in legalset:
                # s[i]='0'
                if s[i - 1 : i + 1] in legalset:
                    # 10,20
                    dp[i] = dp[i - 2]
                else:
                    # '00'
                    return 0
            else:
                # s[i]=1,2..9
                if s[i - 1 : i + 1] in legalset:
                    # 11,23
                    # s[i]可以单独解码,也可以与前一位一起解码
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    # '31'
                    dp[i] = dp[i - 1]
        return dp[-1]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.numDecodings("12")
