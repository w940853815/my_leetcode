#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # 2(010)+5(101)=7(111)
        N_bin = bin(N)[2:]
        length = len(N_bin)
        bin_sum = eval('0b'+'1'*length)
        return bin_sum-N        

        
# @lc code=end

