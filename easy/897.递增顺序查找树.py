#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (72.78%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    48.9K
# Total Submissions: 65.5K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给你一棵二叉搜索树，请你 按中序遍历
# 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# 示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
#
#
# 提示：
#
#
# 树中节点数的取值范围是 [1, 100]
# 0
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 不能使用上面注释的TreeNode类，__main__.TreeNode not valid for TreeNode
        def help(root):
            if root:
                help(root.left)
                res.append(root.val)
                help(root.right)

        res = []
        help(root)
        dummy = TreeNode(-1)
        cur = dummy
        for i in res:
            node = TreeNode(i)
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right


# @lc code=end