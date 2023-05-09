#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#
# https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (71.91%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 40.8K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# 给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。
#
# 保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。
#
# 二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值
# 严格大于 Node.val。
#
# 二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。
#
#
#
# 示例 1：
#
#
#
#
# 输入：preorder = [8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
#
#
# 示例 2:
#
#
# 输入: preorder = [1,3]
# 输出: [1,null,3]
#
#
#
#
# 提示：
#
#
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# preorder 中的值 互不相同
#
#
#
#
#
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            root = TreeNode(preorder.pop(0))
        else:
            return
        left, right = [], []
        for p in preorder:
            if p < root.val:
                left.append(p)
            else:
                right.append(p)
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    res = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
    print(res)
