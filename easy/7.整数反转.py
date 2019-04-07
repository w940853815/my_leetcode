#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.95%)
# Total Accepted:    104.8K
# Total Submissions: 325.4K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#


class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31-1
        MIN = -2**31
        x_string = str(x)
        reverse_str = str()
        if x_string.startswith('-'):
            reverse_str = x_string[::-1]
            no_0_str = Solution.remove_0_char(reverse_str[0:-1])
            reverse_str = '-'+no_0_str
        else:
            reverse_str = x_string[::-1]
            reverse_str = Solution.remove_0_char(reverse_str)
        print(reverse_str)
        if reverse_str=='':
            return 0
        else:
            reverse = int(reverse_str)
        if reverse > MAX or reverse < MIN:
            return 0
        else:
            return reverse

    @staticmethod
    def remove_0_char(str):
        if str.startswith('0'):
            n_str = str[1:]
            return Solution.remove_0_char(n_str)
        else:
            return str
