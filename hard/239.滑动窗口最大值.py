#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.76%)
# Likes:    2282
# Dislikes: 0
# Total Accepted:    435.6K
# Total Submissions: 875.8K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from collections import deque
from typing import List
import heapq

# class MQueue:
#     # 单调队列
#     def __init__(self) -> None:
#         self.queue = []

#     def push(self, val):
#         while self.queue and self.queue[-1] < val:
#             self.queue.pop(-1)
#         self.queue.append(val)

#     def pop(self):
#         print(self.queue)
#         if self.queue:
#             return self.queue.pop(0)

#     def max(self):
#         return self.queue[0]
# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)  # [3,3,5,5,6,7]
    print(res)
