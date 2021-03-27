#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (40.61%)
# Likes:    491
# Dislikes: 0
# Total Accepted:    135.3K
# Total Submissions: 328.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
# 示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 500] 内
# -100
# 0
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        list_len = 0
        cur = head
        if not head or not head.next:
            return head
        while cur:
            list_len += 1
            cur = cur.next
        k %= list_len
        if k == 0:
            return head
        slow = fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head


# @lc code=end
