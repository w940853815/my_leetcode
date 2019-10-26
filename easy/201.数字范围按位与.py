#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        # 二进制位数不一致，必然为0，因为二进制位数少的高位了0，与二进制位数位数多的高位进行与操作必然为0，又因为是连续整数，后面数按位与结果必然也为0，所以就不要计算直接返回0，位数一致再进行按位与操作（一开始解题时直接按位与操作会超时）
        if len(bin(m))!=len(bin(n)):
            return 0
        for x in range(m+1,n+1):
            res = res&x
            # print(res)
        return res
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res=s.rangeBitwiseAnd(0,2147483647)
    print(res)