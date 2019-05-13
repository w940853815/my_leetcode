#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ''
        carry=0
        max_len = len(a) if len(a)>len(b) else len(b)
        # print(max_len)
        a = a.zfill(max_len)[::-1]
        b = b.zfill(max_len)[::-1]
        for a_,b_ in zip(a,b):
            a_ = int(a_)
            b_ = int(b_)
            # print(a_,b_)
            if a_+b_+carry==3:
                carry=1
                sum = sum+str(1)
            elif a_+b_+carry==2:
                carry=1
                sum = sum+str(0)
            elif a_+b_+carry==1:
                carry = 0
                sum = sum + str(1)
            else:
                carry = 0
                sum = sum + str(0)
        if carry == 1:
            return '1'+ sum[::-1]
        else:
            return sum[::-1]


if __name__ == '__main__':
    a='1111'
    b='1111'
    # 10101
    s=Solution()
    data = s.addBinary(a,b)
    print(data)

