#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        preA = list1
        for _ in range(a - 1):
            preA = preA.next
        preB = preA
        for _ in range(b - a + 2):
            preB = preB.next
        preA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = preB
        return list1


# @lc code=end
