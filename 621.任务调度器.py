#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
from collections import Counter
from typing import List
# @lc code=start


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 如果间隔数小于任务数，则返回数组长度
        # 如果间隔数大于等于任务数，则计算结果：(max(相同类出现的次数)-1)*(n+1) + 相同类出现次数最多的类数量
        from collections import Counter
        count = Counter(tasks)
        cnt = len(count)  # 任务数
        max_cnt = max(count.values())  # 相同类出现的最大次数
        max_cnt_tasks = Counter(count.values()).get(max_cnt)  # 相同类出现次数最多的类数量
        res = (max_cnt - 1) * (n + 1) + max_cnt_tasks
        if cnt > n:
            return max(len(tasks), res)
        else:
            return res


if __name__ == "__main__":
    s = Solution()
    t = s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print(t)
# @lc code=end
