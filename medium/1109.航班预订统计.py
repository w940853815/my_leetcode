#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#
# https://leetcode.cn/problems/corporate-flight-bookings/description/
#
# algorithms
# Medium (63.37%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 169.5K
# Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
#
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从
# firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
#
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
#
#
#
# 示例 1：
#
#
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
# 解释：
# 航班编号        1   2   3   4   5
# 预订记录 1 ：   10  10
# 预订记录 2 ：       20  20
# 预订记录 3 ：       25  25  25  25
# 总座位数：      10  55  45  25  25
# 因此，answer = [10,55,45,25,25]
#
#
# 示例 2：
#
#
# 输入：bookings = [[1,2,10],[2,2,15]], n = 2
# 输出：[10,25]
# 解释：
# 航班编号        1   2
# 预订记录 1 ：   10  10
# 预订记录 2 ：       15
# 总座位数：      10  25
# 因此，answer = [10,25]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2 * 10^4
# 1 <= bookings.length <= 2 * 10^4
# bookings[i].length == 3
# 1 <= firsti <= lasti <= n
# 1 <= seatsi <= 10^4
#
#
#
from typing import List
# @lc code=start


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        for book in bookings:
            i = book[0]
            j = book[1]
            val = book[2]
            diff[i-1] += val
            if j < n:
                diff[j] -= val
        for i in range(n):
            res[i] = diff[i]+res[i-1]
        return res


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
    print(res)
    res = s.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2)
    print(res)
