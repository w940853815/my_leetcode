#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])

if __name__ == '__main__':
    s=Solution()
    a=s.lengthOfLastWord('a ')
    print(a)