#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = {}
        alph = "abcdefghijklmnopqrstuvwxyz"
        index = 0
        for k in key:
            if k == " ":
                continue
            if k not in key_map:
                key_map[k] = alph[index]
                index += 1
        res = ""
        for m in message:
            res += key_map.get(m, " ")
        return res


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.decodeMessage(
        "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"
    )
    print(res)
    res = s.decodeMessage(
        "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    )
    print(res)
