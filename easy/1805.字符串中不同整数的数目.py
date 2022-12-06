#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        new_word = ""
        for w in word:
            if ord(w) >= 97 and ord(w) <= 122:
                new_word += " "
            else:
                new_word += w
        new_word = new_word.lstrip().rstrip()
        return len(set([int(i) for i in new_word.split()]))


# @lc code=end
