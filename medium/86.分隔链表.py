#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (64.13%)
# Likes:    699
# Dislikes: 0
# Total Accepted:    210.3K
# Total Submissions: 327.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
# 示例 2：
#
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 200] 内
# -100
# -200
#
#
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(None)
        dummy2 = ListNode(None)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            p = p.next
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next


# @lc code=end
if __name__ == '__main__':
    dummy = ListNode(None)
    p = dummy
    for i in [1, 4, 3, 2, 5, 2]:
        p.next = ListNode(i)
        p = p.next
    head = dummy.next
    s = Solution()
    res = s.partition(head, 3)
    while res:
        print(res.val)
        res = res.next
