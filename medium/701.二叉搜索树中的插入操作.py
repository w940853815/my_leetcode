#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root=TreeNode(val)
        if not root.left and val < root.val:
            root.left = TreeNode(val)
        if not root.right and val > root.val:
            root.right = TreeNode(val)
        if val < root.val:
            self.insertIntoBST(root.left,val)
        if val > root.val:
            self.insertIntoBST(root.right,val)
        return root
# @lc code=end

