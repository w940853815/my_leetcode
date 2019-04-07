#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.64%)
# Total Accepted:    108.2K
# Total Submissions: 321.7K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #根据java解决方法，使用python3实现
        sumHead = ListNode(0)
        p = l1
        q = l2
        curr = sumHead
        carry = 0
        while p!=None or q!=None:
            x = p.val if p!=None else 0
            y = q.val if q!=None else 0
            # print('xval={}'.format(x))
            # print('val={}'.format(y))
            sum = carry + x + y
            # print('sum={}'.format(sum))
            carry = int(sum/10)
            # print('carr=y{}'.format(carry))
            curr.next = ListNode(sum%10)
            # print('curr.next-listnode.val={}'.format(curr.next.val))
            curr = curr.next
            # print('curr-listnode.val={}'.format(curr.val))
            if p!=None:
                p = p.next
            if q!=None:
                q =  q.next
            if carry>0:
                curr.next = ListNode(carry)
            # print('p={}'.format(p))
            # print('q={}'.format(q))
            print('sumHead-listnode.val={}'.format(sumHead.val))
        return sumHead.next


# if __name__ == '__main__':
#     l1 = ListNode(1)
#     l1.next = ListNode(8)
#     l2 = ListNode(0)
#     s = Solution()
#     a=s.addTwoNumbers(l1,l2)
#     while a!=None:
#         print(a.val)
#         a=a.next
    