#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(sentence) == set("abcdefghijklmnopqrstuvwxyz")


# @lc code=end
