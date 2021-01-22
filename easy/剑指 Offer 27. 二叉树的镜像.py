# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def tranvel(root):
            if root:
                root.left, root.right = root.right, root.left
                tranvel(root.left)
                tranvel(root.right)
        tranvel(root)
        return root
