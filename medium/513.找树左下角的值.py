#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode.cn/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (73.75%)
# Likes:    474
# Dislikes: 0
# Total Accepted:    184.5K
# Total Submissions: 250.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#
# 假设二叉树中至少有一个节点。
#
#
#
# 示例 1:
#
#
#
#
# 输入: root = [2,1,3]
# 输出: 1
#
#
# 示例 2:
#
# ⁠
#
#
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [1,10^4]
# -2^31  
#
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        self.res = []

        def bfs():
            while queue:
                self.res = []
                for _ in range(len(queue)):
                    q = queue.pop(0)
                    self.res.append(q.val)
                    if q.left:
                        queue.append(q.left)
                    if q.right:
                        queue.append(q.right)

        bfs()
        return self.res[0]


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([1, 2, 3, 4, None, 5, 6, None, None, 7, None]).main()
    s = Solution()
    res = s.findBottomLeftValue(root)
    print(res)  # 7
    root = List2Tree([1]).main()
    s = Solution()
    res = s.findBottomLeftValue(root)
    print(res)  # 1
    root = List2Tree([1, None, 1]
                     ).main()
    s = Solution()
    res = s.findBottomLeftValue(root)
    print(res)  # 1
    root = List2Tree([0, None, -1]
                     ).main()
    s = Solution()
    res = s.findBottomLeftValue(root)
    print(res)  # -1
    root = List2Tree([2, 1, 3]).main()
    s = Solution()
    res = s.findBottomLeftValue(root)
    print(res)  # 1
