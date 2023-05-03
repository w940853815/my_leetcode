#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode.cn/problems/daily-temperatures/description/
#
# algorithms
# Medium (69.03%)
# Likes:    1475
# Dislikes: 0
# Total Accepted:    422K
# Total Submissions: 611.6K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i
# 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#
#
# 示例 1:
#
#
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#
#
# 示例 2:
#
#
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#
#
# 示例 3:
#
#
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
#
#
# 提示：
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#
from typing import List
# @lc code=start


class Solution:
    def nextGreaterElem(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and nums[i] >= stack[-1][0]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append((nums[i], i))
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = []
        res = self.nextGreaterElem(temperatures)
        for i in range(n):
            if res[i] == -1:
                ans.append(0)
            else:
                ans.append(res[i][1]-i)
        return ans


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
    print(res)  # [1,1,4,2,1,1,0,0]
    res = s.dailyTemperatures(
        temperatures=[34, 80, 80, 34, 34, 80, 80, 80, 80, 34])
    print(res)  # [1,0,0,2,1,0,0,0,0,0]
