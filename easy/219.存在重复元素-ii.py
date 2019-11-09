#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start


class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        res = {}
        for index, item in enumerate(nums):
            # 注意res.get(item)=0时 if条件不会成立
            if item in res:
                if (index - res[item]) <= k:
                    return True
                if index - res[item] > k:
                    res[item] = index
                # return (index - res[item]) == k
            else:
                res[item] = index
        # print(res)
        return False


if __name__ == "__main__":
    s = Solution()
    res = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)

    print(res)
# @lc code=end
