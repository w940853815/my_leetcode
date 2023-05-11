#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
#
# https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (81.56%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 21.9K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
#
#
# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
#
#
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。
#
#
#
# 示例：
#
#
#
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
#
#
#
#
# 提示：
#
#
# 树中节点的数目在 1 到 10^4 之间。
# 每个节点的值在 1 到 100 之间。
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = []

        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            if len(path) >= 3:
                if path[-3] % 2 == 0:
                    res.append(path[-1])
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return sum(res)


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1,
                     4, None, None, None, 5]).main()
    s = Solution()
    res = s.sumEvenGrandparent(root)
    print(res)
