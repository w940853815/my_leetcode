#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.18%)
# Total Accepted:    61.1K
# Total Submissions: 164K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rule = {
            ')':'(',
            ']': '[',
            '}': '{',
        }
        for x in s:
            if len(stack)==0:
                stack.append(x)
            else:
                if rule.get(x)==stack[-1]:
                    stack.pop()
                else:
                    stack.append(x)

        if len(stack)>0:
            return False
        else:
            return  True


if __name__== '__main__':
    s=Solution()
    a=s.isValid('{[]}')
    print(a)
        

