#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (63.44%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    174.8K
# Total Submissions: 275.6K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
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
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
#
#
#
#
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = []
        min_val = float('inf')

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in range(1, len(self.res)):
            dif = abs(self.res[i]-self.res[i-1])
            if dif < min_val:
                min_val = dif
        return min_val


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([236, 104, 701, None, 227, None, 911]
                     ).main()
    s = Solution()
    res = s.getMinimumDifference(root)
    print(res)
