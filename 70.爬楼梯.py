#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1 :
        #     return 1
        # if n == 2:
        #     return 2
        # return Solution().climbStairs(n-1)+Solution().climbStairs(n-2)
        res = []
        res.append(1)
        res.append(2)
        if n==1:
            return res[0]
        if n==2:
            return res[1]
        for i in range(2,n):
            tmp = res[i-1]+res[i-2]
            res.append(tmp)
        return res[n-1]

if __name__ == "__main__":
    s =  Solution()
    a = s.climbStairs(2)
    # print(a)
