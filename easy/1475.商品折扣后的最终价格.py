#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from typing import List

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i, price in enumerate(prices):
            flag = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    flag = True
                    res.append(prices[i] - prices[j])
                    break
            if not flag:
                res.append(price)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.finalPrices([8, 4, 6, 2, 3])
    print(res)
# @lc code=end
