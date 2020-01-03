#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        # # print(self.cache)
        # if len(s) == 1:
        #     return s
        # # Time Limit Exceeded

        # def is_palindroem(s):
        #     if self.cache.get(s):
        #         return self.cache.get(s)
        #     else:
        #         self.cache[s] = (s == s[::-1])
        #         return s == s[::-1]
        # if is_palindroem(s):
        #     return s
        # if is_palindroem(s[1:]):
        #     return s[1:]
        # if is_palindroem(s[:-1]):
        #     return s[:-1]
        # s1 = self.longestPalindrome(s=s[1:])

        # s2 = self.longestPalindrome(s=s[:-1])
        # if len(s1) > len(s2):
        #     return s1
        # else:
        #     return s2
        # print('s1' + s1)
        # print('s2' + s2)

         # 中心扩散法Spread From Center
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            # 当前找到的最长回文子串
            print(palindrome_odd)
            print(palindrome_even)
            res = max(palindrome_odd, palindrome_even, res, key=len)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.longestPalindrome('sabaw')
    print(res)
