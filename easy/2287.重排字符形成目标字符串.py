#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#
from collections import Counter

# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = Counter(s)
        tc = Counter(target)
        res_min = float("inf")
        for k, v in tc.items():
            if sc.get(k):
                tmp = sc[k] // tc[k]
                if res_min > tmp:
                    res_min = tmp
            else:
                return 0
        return res_min


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.rearrangeCharacters("ilovecodingonleetcode", "code")
    print(res)
    res = s.rearrangeCharacters("abcba", "abc")
    print(res)
    res = s.rearrangeCharacters("abbaccaddaeea", "aaaaa")
    print(res)
