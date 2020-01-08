#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Limit Exceeded
        # [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]
        # res = []
        # data=[]
        # for index_i, i in enumerate(nums):
        #     for index_j, j in enumerate(nums[index_i:]):
        #         try:
        #             z=-(i+j)
        #             index_z = nums.index(-(i + j))
        #             if index_i != index_z and index_j != index_z and index_i != index_j:
        #                 three_num = [nums[index_i],nums[index_j],nums[index_z]]
        #                 if set(three_num) not in res:
        #                     res.append(set(three_num))
        #                     data.append(three_num)
        #         except ValueError:
        #             pass
        # return data

        # 1. 特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
        # 2.对数组进行排序。
        # 3.遍历排序后数组：
        #     1.若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于0，直接返回结果。
        #     2.对于重复元素：跳过，避免出现重复解
        #     3.令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
        #         1.当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
        #         2.若和大于 0，说明 nums[R] 太大，R 左移
        #         3.若和小于 0，说明 nums[L] 太小，L 右移
        if len(nums)<3:
            return []
        nums.sort()
        res = []
        for index,num in enumerate(nums):
            if(nums[index]>0):
                return res
            if(index>0 and nums[index]==nums[index-1]):
                continue
            L=index+1
            R=len(nums)-1
            while L<R:
                
                sum=num+nums[L]+nums[R]
                if sum==0:
                    res.append([num,nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L+=1
                    R-=1
                if sum<0:
                    L+=1
                if sum>0:
                    R-=1
        return res


if __name__ == "__main__":
    s = Solution()
    res=s.threeSum([-1, 0, 1, 2, -1, -4])
    
    print(res)

# @lc code=end
