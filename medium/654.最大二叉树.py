#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode.cn/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (82.67%)
# Likes:    683
# Dislikes: 0
# Total Accepted:    196.1K
# Total Submissions: 237.3K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
#
#
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
#
#
# 返回 nums 构建的 最大二叉树 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
# ⁠   - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
# ⁠       - 空数组，无子节点。
# ⁠       - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
# ⁠           - 空数组，无子节点。
# ⁠           - 只有一个元素，所以子节点是一个值为 1 的节点。
# ⁠   - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
# ⁠       - 只有一个元素，所以子节点是一个值为 0 的节点。
# ⁠       - 空数组，无子节点。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1]
# 输出：[3,null,2,null,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同
#
#
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        _len = len(nums)
        max_val = max(nums)
        max_index = nums.index(max_val)
        left_list = [nums[i] for i in range(max_index)]
        right_list = [nums[i] for i in range(max_index+1, _len)]
        tree_node = TreeNode(max_val)
        tree_node.left = self.constructMaximumBinaryTree(left_list)
        tree_node.right = self.constructMaximumBinaryTree(right_list)
        return tree_node

# @lc code=end
