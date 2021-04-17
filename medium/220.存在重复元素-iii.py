#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (26.59%)
# Likes:    402
# Dislikes: 0
# Total Accepted:    47.3K
# Total Submissions: 172.1K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
# ，同时又满足 abs(i - j)  。
#
# 如果存在则返回 true，不存在返回 false。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
#
# 示例 2：
#
#
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
#
# 示例 3：
#
#
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
#
#
#
# 提示：
#
#
# 0
# -2^31
# 0
# 0
#
#
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            # t=3 桶内元素可以为0,1,2,3 最大和最小差值为t
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False


# @lc code=end
