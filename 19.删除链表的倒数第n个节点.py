#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def length(head):
            """返回链表长度"""
            cur = head
            count = 0
            while cur:
                count += 1
                cur = cur.next
            return count
        count = length(head)
        remove_pos = count - n   # 删除位置,从0开始数
        pos = 0  # 当前位置，从0开始
        cur = head
        pre = None  # cur前一个节点
        while cur:
            if remove_pos == 0:  # 第一个节点
                head = cur.next
                break
            if pos == remove_pos:
                pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
            pos += 1

        return head
