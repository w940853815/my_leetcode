#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        res = ''
        if str == '' or str == '-' or str == '+':
            return 0
        if str.startswith('-') or str.startswith('+'):
            res = str[0]
            for i in str[1:]:
                if i.isdigit():
                    res += i
                else:
                    break
        elif not str[0].isnumeric():
            return 0
        else:
            for i in str:
                if i.isdigit():
                    res += i
                else:
                    break
        try:
            int(res)
        except ValueError:
            return 0
        if int(res) < -2**31:
            res = -2**31
        if int(res) > 2**31 - 1:
            res = 2**31 - 1

        return int(res)


if __name__ == "__main__":
    s = Solution()
    res = s.myAtoi('+-2')
    print(res)

# @lc code=end
