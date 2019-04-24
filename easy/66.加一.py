#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: list) -> list:
        n_list = []
        carry = None
        sum = None
        for index, d in enumerate(digits[::-1]):
            if index == 0:
                carry = (d + 1) // 10
                sum = (d + 1) % 10
            else:
                sum = (d + carry) % 10
                carry = (d + carry) // 10
            n_list.append(sum)
        if carry == 1:
            n_list.append(1)
        return n_list[::-1]


if __name__ == '__main__':
    s = Solution()
    digits = [9, 9, 9, 9]
    a = s.plusOne(digits)
    print(a)
