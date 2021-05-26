#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (57.92%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    30.7K
# Total Submissions: 47.7K
# Testcase Example:  '"(abcd)"'
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
# 注意，您的结果中 不应 包含任何括号。
#
#
#
# 示例 1：
#
# 输入：s = "(abcd)"
# 输出："dcba"
#
#
# 示例 2：
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"
#
#
# 示例 3：
#
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#
#
# 示例 4：
#
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
#
#
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ""
        stack = []
        for i in s:
            if i == "(":
                stack.append(res)
                res = ""
            elif i == ")":
                res = res[::-1]
                res = stack.pop() + res
            else:
                res += i

        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.reverseParentheses("(abcd)")
    print(res)