# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            print(left, right)
            print()
            while not self.is_even(nums[left]) and left < right:
                left += 1
            while self.is_even(nums[right]) and left < right:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return nums

    def is_even(self, num):
        # 4 2 1
        return (num & 1) == 0


if __name__ == "__main__":
    s = Solution()
    ret = s.exchange([1, 3, 5])
    print(ret)
