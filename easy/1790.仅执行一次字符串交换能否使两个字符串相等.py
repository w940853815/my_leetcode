#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        if s1 == s2:
            return True
        _len = len(s1)
        for i in range(_len):
            for j in range(i + 1, _len):
                s2_list = [s for s in s2]
                s2_list[i], s2_list[j] = s2_list[j], s2_list[i]
                if s1 == "".join(s2_list):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    res = s.areAlmostEqual("bank", "kanb")
    print(res)
# @lc code=end
