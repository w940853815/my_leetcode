#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start


class Solution:
    def compress(self, chars: list) -> int:
        # 处理chars最后一个元素
        chars.append('^')
        pre_char = chars[0]
        count = 0
        index = 0
        for char in chars:

            if char == pre_char:
                count += 1
            else:
                chars[index] = pre_char
                index += 1
                if count > 1:
                    for s in str(count):
                        chars[index] = s
                        index += 1
                pre_char = char
                count = 1
        return index


if __name__ == "__main__":
    s = Solution()
    chars = ["a", "b", "b", "b", "b", "b",
             "b", "b", "b", "b", "b", "b", "b"]
    s.compress(chars)
    print(chars)
# @lc code=end
