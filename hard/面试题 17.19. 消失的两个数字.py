# 给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

# 以任意顺序返回这两个数字均可。
# 示例 1:

# 输入: [1]
# 输出: [2,3]
# 示例 2:

# 输入: [2,3]
# 输出: [1,4]

from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return [1, 2]
        max_num = len(nums) + 2
        miss_sum = (1 + max_num) * max_num / 2 - sum(nums)
        miss_mid_num = miss_sum // 2
        mid_sum = 0
        print(miss_sum)
        for num in nums:
            if num <= miss_mid_num:
                mid_sum += num
        x = (1 + miss_mid_num) * (miss_mid_num) // 2 - mid_sum
        y = miss_sum - x
        return [int(x), int(y)]


if __name__ == "__main__":
    s = Solution()
    res = s.missingTwo([2, 3])
    # res = s.missingTwo([1])
    print(res)
