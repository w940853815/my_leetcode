#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (54.48%)
# Likes:    635
# Dislikes: 0
# Total Accepted:    156.2K
# Total Submissions: 286.3K
# Testcase Example:  '[1,null,2,2]'
#
# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
#
# 如果树中有不止一个众数，可以按 任意顺序 返回。
#
# 假定 BST 满足如下定义：
#
#
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
#
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,2]
# 输出：[2]
#
#
# 示例 2：
#
#
# 输入：root = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [1, 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
#
#
from typing import List, Optional
from collections import Counter
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()
        res = []

        def dfs(root):
            if not root:
                return
            count[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        max_count = max(count.values())
        for k, v in count.items():
            if v == max_count:
                res.append(k)
        return res


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([1, None, 2, 2, None]).main()
    s = Solution()
    res = s.findMode(root)
    print(res)
