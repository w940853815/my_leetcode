#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (53.63%)
# Total Accepted:    57.4K
# Total Submissions: 106.9K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # res = ListNode(None)
        # l3 = res
        # while not (l1.next==None and l2.next==None):
        #     if l1.val <= l2.val:
        #         l3.next= l1
        #         l1 = l1.next
        #         # if l3==None:
        #         #     l3= ListNode(l1.val)
        #         # else:
        #         #     temp = ListNode(l1.val)
        #         #     l1 = l1.next
        #     else:
        #         l3.next = l2
        #         l2 = l2.next
        #     l3= l3.next
        """
        不明白
        """
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1=l1.next
            else:
                node.next= l2
                l2=l2.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


    # return  res.next

if __name__=='__main__':
    s=Solution()
    l1 = ListNode(1)
    l1.next=ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(2)
    l3 = s.mergeTwoLists(l1,l2)
    while l3:
        print(l3.val)
        l3 = l3.next
