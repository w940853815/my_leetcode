#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#
from collections import Counter

# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i in range(len(num)):
            if count[str(i)] != int(num[i]):
                return False
        return True


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.digitCount("1210")
    print(res)
    res = s.digitCount("030")
    print(res)
