#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.58%)
# Total Accepted:    66.9K
# Total Submissions: 204.8K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        str_min = 0
        for s in strs:
            if str_min<len(s):
                str_min = len(s)
        if str_min==0:
            return ""
        for x in range(1,str_min+1):
            prefix = strs[0][:x]
            for s in strs:
                if not s.startswith(prefix):
                    if x==0:
                        return ""
                    else:
                        # print(x)
                        # print(strs)
                        return strs[0][:x-1]
        return prefix

if __name__ == "__main__":
    s=Solution()
    a = s.longestCommonPrefix(["c","acc","ccc"])
    print(a)

