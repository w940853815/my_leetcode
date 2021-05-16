#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (60.18%)
# Likes:    333
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 39.8K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：0
#
#
# 示例 3：
#
#
# 输入：nums = [2,4]
# 输出：6
#
#
# 示例 4：
#
#
# 输入：nums = [8,10,2]
# 输出：10
#
#
# 示例 5：
#
#
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#
#
#
# @lc code=start

from typing import List


class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 构造前缀树
        size = len(format(max(nums), "b")) - 1
        root = Trie(-1)
        for num in nums:
            cur = root
            for i in range(size, -1, -1):
                v = (num >> i) & 1
                if v not in cur.child:
                    cur.child[v] = Trie(v)
                cur = cur.child[v]
        # 搜索
        res = 0
        for num in nums:
            cur = root
            total = 0
            for i in range(size, -1, -1):
                v = (num >> i) & 1
                if 1 - v in cur.child:
                    total = total * 2 + 1
                    cur = cur.child[1 - v]
                else:
                    total = total * 2
                    cur = cur.child[v]
            res = max(res, total)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.findMaximumXOR([3, 10, 5, 25, 2, 8])
    print(res)