#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (57.71%)
# Likes:    2416
# Dislikes: 0
# Total Accepted:    634.5K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
#
#
#
from queue import PriorityQueue
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue
        dummy = p = ListNode(None)
        index = 0
        pq = PriorityQueue()
        for l in lists:
            # 防止r.val 相同，拿ListNode对象比大小
            if l:
                pq.put([l.val, index, l])
                index += 1
        while not pq.empty():
            val, _, node = pq.get()
            p.next = ListNode(val)
            p = p.next
            node = node.next
            if node:
                pq.put([node.val, index, node])
                index += 1
        return dummy.next


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    test_case = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for tcs in test_case:
        dummy = p = ListNode(None)
        for tc in tcs:
            p.next = ListNode(tc)
            p = p.next
        lists.append(dummy.next)
    res = s.mergeKLists(lists)
    p = res
    while p:
        print(p.val)
        p = p.next
