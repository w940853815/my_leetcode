#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#
# https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/description/
#
# algorithms
# Hard (42.25%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 30.9K
# Testcase Example:  '[3,2,3]\n3'
#
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间
# 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
# 返回分配方案中尽可能 最小 的 最大工作时间 。
#
#
#
# 示例 1：
#
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#
#
# 示例 2：
#
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#
from typing import List

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(array, limit, groups):
            if not array:
                return True
            job = array.pop()
            for i in range(k):
                if groups[i] + job <= limit:
                    groups[i] += job
                    if backtrack(array, limit, groups):
                        return True
                    groups[i] -= job
                    if groups[i] == 0:
                        break
            array.append(job)
            return False

        def check(limit):
            array = sorted(jobs)
            groups = [0] * k
            if backtrack(array, limit, groups):
                return True
            else:
                return False

        left = max(jobs)
        right = sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end
