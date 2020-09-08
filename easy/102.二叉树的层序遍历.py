#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (62.96%)
# Likes:    624
# Dislikes: 0
# Total Accepted:    190.6K
# Total Submissions: 300.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while len(queue):
            tmp = []
            for i in range(len(queue)):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res

# @lc code=end
