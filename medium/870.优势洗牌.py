#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode.cn/problems/advantage-shuffle/description/
#
# algorithms
# Medium (50.26%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    63.8K
# Total Submissions: 126.8K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i
# 的数目来描述。
#
# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。
#
#
#
# 示例 1：
#
#
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
#
#
# 示例 2：
#
#
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
#
#
#
#
# 提示：
#
#
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9
#
#
#
from typing import List
# @lc code=start


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from queue import PriorityQueue
        maxpq = PriorityQueue()
        n = len(nums1)
        res = [0]*n
        for i in range(n):
            maxpq.put((-nums2[i], i))
        nums1.sort()
        left, right = 0, n-1
        while not maxpq.empty():
            max_val, index = maxpq.get()
            max_val = -max_val
            if nums1[right] > max_val:
                res[index] = nums1[right]
                right -= 1
            else:
                res[index] = nums1[left]
                left += 1
        return res


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    res = s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11])
    print(res)
    res = s.advantageCount(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11])
    print(res)
