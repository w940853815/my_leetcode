#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#
from collections import defaultdict

# @lc code=start
class Solution:
    # Time Limit Exceeded
    # def beautySum(self, s: str) -> int:
    #     len_str = len(s)
    #     res = 0
    #     for i in range(len_str):
    #         for j in range(len_str):
    #             tmp_s = s[i : j + 1]
    #             if len(tmp_s):
    #                 c = Counter(tmp_s).values()
    #                 _max = max(c)
    #                 _min = min(c)
    #                 res += _max - _min

    #     return res

    def beautySum(self, s: str) -> int:
        len_str = len(s)
        res = 0
        for i in range(len_str):
            cnt = defaultdict(int)
            mx = 0
            for j in range(i, len_str):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                mn = min(cnt.values())
                res += mx - mn
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.beautySum("aabcb")
    assert res == 5
    res = s.beautySum("aabcbaa")
    assert res == 17
