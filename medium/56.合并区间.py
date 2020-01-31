#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        flag = True
        intervals.sort(key=lambda i: i[0])

        def _meger(intervals):
            index = 0
            for item in intervals:
                if index < len(intervals) - 1:
                    next_item = intervals[index + 1]
                    # 重叠
                    if item[1] <= next_item[1] and item[1] >= next_item[0]:
                        min_ = item[0]
                        max_ = next_item[1]
                        intervals[index] = [min_, max_]
                        del intervals[index + 1]
                        return True
                    # [[1, 4], [2, 3]]
                    if item[0] <= next_item[0] and item[1] >= next_item[1]:
                        min_ = item[0]
                        max_ = item[1]
                        intervals[index] = [min_, max_]
                        del intervals[index + 1]
                        return True
                    else:
                        pass
                index += 1
            return False
        while flag:
            flag = _meger(intervals)
        return intervals


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.merge([[1, 4], [2, 3]])
    print(res)
