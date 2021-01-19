# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 遍历
        for index in range(1, len(numbers)):
            if numbers[index] < numbers[index-1]:
                return numbers[index]
        return numbers[0]
