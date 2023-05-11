#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] 二叉树中的链表
#
# https://leetcode.cn/problems/linked-list-in-binary-tree/description/
#
# algorithms
# Medium (43.66%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 54.8K
# Testcase Example:  '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
#
# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
#
# 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False
# 。
#
# 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [4,2,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# 输出：true
# 解释：树中蓝色的节点构成了与链表对应的子路径。
#
#
# 示例 2：
#
#
#
# 输入：head = [1,4,2,6], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# 输出：true
#
#
# 示例 3：
#
# 输入：head = [1,4,2,6,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# 输出：false
# 解释：二叉树中不存在一一对应链表的路径。
#
#
#
#
# 提示：
#
#
# 二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
# 链表包含的节点数目在 1 到 100 之间。
# 二叉树包含的节点数目在 1 到 2500 之间。
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
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Time Limit Exceeded
        # 55/67 cases passed (N/A)
        # head_list = []
        # cur = head
        # while cur:
        #     head_list.append(cur.val)
        #     cur = cur.next
        # self.is_sub = False

        # def is_sub_list(l1, l2):
        #     len_l1 = len(l1)
        #     for i in range(len_l1):
        #         for j in range(i, len_l1):
        #             if l2 == l1[i:j+1]:
        #                 return True
        #     return False

        # def dfs(root, path):
        #     if not root:
        #         return
        #     path.append(root.val)
        #     if len(path) >= len(head_list):
        #         if is_sub_list(path, head_list):
        #             self.is_sub = True
        #     dfs(root.left, path)
        #     dfs(root.right, path)
        #     path.pop()
        # dfs(root, [])
        # return self.is_sub
        def dfs(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right)
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# @lc code=end
if __name__ == '__main__':
    from utils.link_node import create_linked_list
    from utils.tree_node import List2Tree
    head = create_linked_list([4, 2, 8])
    root = List2Tree([1, 4, 4, None, 2, 2, None, 1, None,
                     6, 8, None, None, None, None, 1, 3]).main()
    s = Solution()
    res = s.isSubPath(head, root)
    print(res)
