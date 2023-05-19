#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#
# https://leetcode.cn/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (70.86%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    80.2K
# Total Submissions: 113.1K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
#
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
#
#
#
# 示例 1：
#
#
#
# 输入：[1,1,1,1,1,null,1]
# 输出：true
#
#
# 示例 2：
#
#
#
# 输入：[2,2,2,5,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 给定树的节点数范围是 [1, 100]。
# 每个节点的值都是整数，范围为 [0, 99] 。
#
#
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = root.val

        def dfs(root):
            if not root:
                return True
            if self.val != root.val:
                return False
            return dfs(root.left) and dfs(root.right)
        return dfs(root)

# @lc code=end
