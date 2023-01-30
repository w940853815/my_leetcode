#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while slow:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


# @lc code=end
