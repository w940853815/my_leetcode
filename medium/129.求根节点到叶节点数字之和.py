#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pretotal):
            if not root:
                return 0
            pretotal = pretotal * 10 + root.val
            if not root.left and not root.right:
                return pretotal
            else:
                return dfs(root.left, pretotal) + dfs(root.right, pretotal)

        return dfs(root, 0)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    res = s.sumNumbers(t1)
    print(res)
