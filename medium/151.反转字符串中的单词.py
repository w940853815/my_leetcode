#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split(' ')
        while '' in sl:
            sl.remove('')
        return ' '.join(sl[::-1]).rstrip().lstrip()
# @lc code=end

if __name__ == "__main__":
    s=Solution()
    res=s.reverseWords("the sky is blue")
    print(res)
    res=s.reverseWords("  hello world  ")
    print(res)
    res=s.reverseWords("a good   example")
    print(res)