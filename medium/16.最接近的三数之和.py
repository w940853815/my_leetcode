#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        target_dist = float('inf')
        if len(nums) == 3:
            return sum(nums)
        res = None
        for i, _ in enumerate(nums):
            L = i + 1
            R = len(nums) - 1
            # if nums[i] == nums[i - 1]:
            #     continue
            while L < R:
                _sum = nums[i] + nums[L] + nums[R]
                distince = abs(_sum - target)
                if _sum == target:
                    return _sum
                if _sum < target:
                    L += 1
                if _sum > target:
                    R -= 1
                if target_dist > distince:
                    target_dist = distince
                    res = _sum
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.threeSumClosest([1, 1, 1, 1], 0)

    print(res)

# @lc code=end
