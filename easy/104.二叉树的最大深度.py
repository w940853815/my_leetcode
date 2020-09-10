#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (73.48%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    272K
# Total Submissions: 362.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
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

    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return []
        queue = [root]
        while len(queue):
            for i in range(len(queue)):
                r = queue.pop(0)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            depth += 1
        return depth
# @lc code=end
