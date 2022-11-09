#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
from typing import List

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for w in "".join(set(word)):
                if w not in allowed:
                    flag = False
            if flag:
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"])
    print(res)
