#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.39%)
# Likes:    910
# Dislikes: 0
# Total Accepted:    258.8K
# Total Submissions: 582.9K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
# 示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
#
#
#
from collections import Counter
# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        need = Counter(s1)
        window = Counter()
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right-left >= len(s1):
                if len(need) == valid:
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.checkInclusion("ab", "eidbaooo")
    print(res)
    res = s.checkInclusion("ab", "eidboaoo")
    print(res)
