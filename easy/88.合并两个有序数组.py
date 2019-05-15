#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
class Solution:
    def merge(self, nums1:list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()

if __name__ == "__main__":
    nums1 =[1,2,3,0,0,0]
    nums2 = [2,5,6]
    s=Solution()
    s.merge(nums1,3,nums2,3)

    print(nums1)