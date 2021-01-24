#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (38.32%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    52.7K
# Total Submissions: 137.6K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        s1_len, s2_len = len(s1), len(s2)
        s1_char_count = Counter(s1)
        print(s1_char_count)
        for i in range(0, s2_len - s1_len + 1):
            print(i, i + s1_len - 1)
            if Counter(s2[i : i + s1_len]) == s1_char_count:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.checkInclusion("adc", "dcda")
    print(res)
