#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_data =[]
        def recurse(node):
            if node != None:
                if node.left:
                    #当节点为叶子节点才添加到列表中
                    if node.left.left==None and node.left.right==None:
                        left_data.append(node.left.val)
                recurse(node.left)
                recurse(node.right)
        recurse(root)
        return sum(left_data)
        
# @lc code=end

