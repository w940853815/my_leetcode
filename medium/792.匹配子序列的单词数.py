#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
from typing import List

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            flag = True
            start_index = 0
            for w in word:
                index = s[start_index:].find(w)
                if index > -1:
                    start_index = start_index + index + 1
                else:
                    flag = False
                    break
            if flag:
                res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
    print(res)
    assert res == 3
    res = s.numMatchingSubseq(
        "dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    )
    print(res)
    assert res == 2
    res = s.numMatchingSubseq(
        "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac",
        [
            "wpddkvbnn",
            "lnagtva",
            "kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju",
            "rwpddkvbnnugln",
            "gloeofnpjqlkdsqvruvabjrikfwronbrdyyj",
            "vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos",
            "mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina",
            "rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip",
            "fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq",
            "qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx",
        ],
    )
    print(res)
    assert res == 5
