#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode.cn/problems/path-sum-ii/description/
#
# algorithms
# Medium (63.18%)
# Likes:    970
# Dislikes: 0
# Total Accepted:    343.4K
# Total Submissions: 543.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
#
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点总数在范围 [0, 5000] 内
# -1000
# -1000
#
#
#
#
#
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    # 对象可变，导致path返回时变为空
                    res.append(list(path))
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return res


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]).main()
    s = Solution()
    res = s.pathSum(root, 22)
    print(res)
