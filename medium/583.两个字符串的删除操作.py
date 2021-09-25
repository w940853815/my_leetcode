#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (58.70%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 71.2K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
#
#
#
# 示例：
#
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
#
#
#
#
# 提示：
#
#
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
#
#
#
from collections import defaultdict

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 最长公共子序列
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.minDistance("leetcode", "etco")
    assert res == 4
    res = s.minDistance("sea", "eat")
    assert res == 2
    res = s.minDistance("sea", "ate")
    assert res == 4
