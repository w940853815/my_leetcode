#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (56.31%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    54.5K
# Total Submissions: 92.6K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 注意：本题与
# 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
#
#
#
#
#
# 示例 1：
#
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [2, 100] 内
# 0
#
#
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
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(root, res):
            if root:
                dfs(root.left, res)
                res.append(root.val)
                dfs(root.right, res)

        res = []
        dfs(root, res)
        min_res = float("inf")
        for index in range(1, len(res)):
            min_res = min(min_res, res[index] - res[index - 1])
        return min_res


# @lc code=end
