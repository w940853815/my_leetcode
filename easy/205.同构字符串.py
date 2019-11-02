#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = {}
        for index, i in enumerate(s):
            j = t[index]
            if res.get(i):
                if res.get(i) != j:
                    return False
            else:
                res[i] = j
        # 两个字符不能映射到同一个字符上
        if len(set(res.keys())) != len(set(res.values())):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    res = s.isIsomorphic('ab', 'aa')
    print(res)

# @lc code=end
