#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#
# https://leetcode.cn/problems/determine-if-string-halves-are-alike/description/
#
# algorithms
# Easy (78.52%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    29.8K
# Total Submissions: 38K
# Testcase Example:  '"book"'
#
# 给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
#
# 两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s
# 可能同时含有大写和小写字母。
#
# 如果 a 和 b 相似，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：s = "book"
# 输出：true
# 解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。
#
#
# 示例 2：
#
#
# 输入：s = "textbook"
# 输出：false
# 解释：a = "text" 且 b = "book" 。a 中有 1 个元音，b 中有 2 个元音。因此，a 和 b 不相似。
# 注意，元音 o 在 b 中出现两次，记为 2 个。
#
#
#
#
# 提示：
#
#
# 2 <= s.length <= 1000
# s.length 是偶数
# s 由 大写和小写 字母组成
#
#
#

# @lc code=start


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def find_yuanyin_count(text):
            count = 0
            for i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count = count + text.count(i)
            return count
        s_len = len(s)
        a = s[:int(s_len/2)]
        b = s[int(s_len/2):]
        return find_yuanyin_count(a) == find_yuanyin_count(b)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    res = s.halvesAreAlike("textbook")
    assert res == False
    res = s.halvesAreAlike("book")
    assert res == True
