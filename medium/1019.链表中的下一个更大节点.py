#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#
# https://leetcode.cn/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (64.28%)
# Likes:    305
# Dislikes: 0
# Total Accepted:    52.9K
# Total Submissions: 82.2K
# Testcase Example:  '[2,1,5]'
#
# 给定一个长度为 n 的链表 head
#
# 对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
#
# 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i
# 个节点没有下一个更大的节点，设置 answer[i] = 0 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：head = [2,1,5]
# 输出：[5,5,0]
#
#
# 示例 2：
#
#
#
#
# 输入：head = [2,7,4,3,5]
# 输出：[7,0,5,5,0]
#
#
#
#
# 提示：
#
#
# 链表中节点数为 n
# 1 <= n <= 10^4
# 1 <= Node.val <= 10^9
#
#
#
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        stack = []
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            n += 1
        ans = [0]*n
        pr = pre
        i = n-1
        while pr:
            while stack and stack[-1] <= pr.val:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(pr.val)
            pr = pr.next
            i -= 1
        return ans


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l2 = ListNode(1)
    l3 = ListNode(5)
    l1.next = l2
    l2.next = l3
    res = s.nextLargerNodes(l1)
    print(res)
