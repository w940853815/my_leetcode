#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool: 
        while n:
            if n % 3 == 2:
                return False
            n = n // 3
        return True

# @lc code=end

if __name__ == '__main__':
    s=Solution()
    res = s.checkPowersOfThree(12)
    assert res is True
    res = s.checkPowersOfThree(21)
    assert res is False



