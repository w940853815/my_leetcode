#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (66.36%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    119K
# Total Submissions: 179.3K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
#
#
#
# 示例1：
#
#
#
#
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#
#
# 示例2：
#
#
# 输入: root = [1,2,3]
# 输出: [1,3]
#
#
#
#
# 提示：
#
#
# 二叉树的节点个数的范围是 [0,10^4]
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
#
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            size = len(q)
            max_val = float('-inf')
            for i in range(size):
                r = q.pop(0)
                max_val = max(r.val, max_val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            res.append(max_val)
        return res


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([1, 3, 2, 5, 3, None, 9]).main()
    s = Solution()
    res = s.largestValues(root)
    print(res)
