#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time Limit Exceeded
        # for x in s:
        #     if s.count(x) == 1:
        #         return s.find(x)
        # return -1
        res = {}
        for x in s:
            if res.get(x) == None:
                res[x] = 1
            else:
                res[x] += 1
        for index, x in enumerate(s):
            if res[x] == 1:
                return index
        return -1


if __name__ == "__main__":
    s = Solution()
    res = s.firstUniqChar('leetcode')
    print(res)

# @lc code=end
