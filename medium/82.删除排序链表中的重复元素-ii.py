#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (50.44%)
# Likes:    565
# Dislikes: 0
# Total Accepted:    119.8K
# Total Submissions: 231.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
# 返回同样按升序排列的结果链表。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100
# 题目数据保证链表已经按升序排列
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dumy = ListNode(0, head)
        cur = dumy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                dup_el = cur.next.val
                while cur.next and cur.next.val == dup_el:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dumy.next


# @lc code=end
