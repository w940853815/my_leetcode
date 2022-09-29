# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

# 示例1:

#  输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
# 示例2:

#  输入：s1 = "aa", s2 = "aba"
#  输出：False


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        str_len = len(s1)
        for i in range(str_len):
            if s1 == s2[i + 1 :] + s2[: i + 1]:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    res = s.isFlipedString("waterbottle", "erbottlewat")
    print(res)
