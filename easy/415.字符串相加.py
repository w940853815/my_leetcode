#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        if len(num1) > len(num2):
            num2 = num2.zfill(len(num1))
        else:
            num1 = num1.zfill(len(num2))
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]

        for n1, n2 in zip(num1, num2):
            n1, n2 = int(n1), int(n2)
            if n1 + n2 + carry >= 10:
                stmp = n1 + n2 + carry - 10
                carry = 1
            else:
                stmp = n1 + n2 + carry
                carry = 0
            res += str(stmp)
        if int(num1[-1]) + int(num2[-1]) + carry >= 10:
            res += '1'
        return res[:: -1]


if __name__ == "__main__":
    s = Solution()
    res = s.addStrings('1', '9')
    print(res)
    # @lc code=end
