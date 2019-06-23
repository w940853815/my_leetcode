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
    # 循环一次，采用双指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head
        first, second = dump, dump

        for i in range(1, n+2):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dump.next

    # 循环两次，第一次求链表长度，第二次转换为删
    # 除length-n节点问题
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     def length(head):
    #         """返回链表长度"""
    #         cur = head
    #         count = 0
    #         while cur:
    #             count += 1
    #             cur = cur.next
    #         return count
    #     count = length(head)
    #     remove_pos = count - n   # 删除位置,从0开始数
    #     pos = 0  # 当前位置，从0开始
    #     cur = head
    #     pre = None  # cur前一个节点
    #     while cur:
    #         if remove_pos == 0:  # 第一个节点
    #             head = cur.next
    #             break
    #         if pos == remove_pos:
    #             pre.next = cur.next
    #             break
    #         else:
    #             pre = cur
    #             cur = cur.next
    #         pos += 1
    #     return head
