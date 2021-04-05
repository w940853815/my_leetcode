#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (49.53%)
# Likes:    840
# Dislikes: 0
# Total Accepted:    308.2K
# Total Submissions: 616.8K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自
# nums2 的元素。
#
#
#
# 示例 1：
#
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#
#
# 示例 2：
#
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#
#
#
#
# 提示：
#
#
# nums1.length == m + n
# nums2.length == n
# 0
# 1
# -10^9
#
#
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        p, q = 0, 0
        while p < m or q < n:
            print(p, q)
            if p == m:
                res.append(nums2[q])
                q += 1
            elif q == n:
                res.append(nums1[p])
                p += 1
            elif nums1[p] <= nums2[q]:
                res.append(nums1[p])
                p += 1
            else:
                res.append(nums2[q])
                q += 1
        nums1[: m + n] = res
        return nums1[: m + n]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(res)
