#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#
# https://leetcode.cn/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (62.36%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 116.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。
#
# 空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#
#
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4]
# 输出："1(2(4))(3)"
# 解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3,null,4]
# 输出："1(2()(4))(3)"
# 解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。
#
#
#
# 提示：
#
#
# 树中节点的数目范围是 [1, 10^4]
# -1000 <= Node.val <= 1000
#
#
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.s = ''

        def dfs(root):
            if not root:
                return
            self.s += f"({root.val}"
            if not root.left and root.right:
                self.s += "()"
            dfs(root.left)
            dfs(root.right)
            self.s += ")"
        dfs(root)
        return self.s[1:-1]


# @lc code=end
if __name__ == '__main__':
    from utils.tree_node import List2Tree
    root = List2Tree([1, 2, 3, 4, None]).main()
    s = Solution()
    res = s.tree2str(root)
    assert res == "1(2(4))(3)"
    root = List2Tree([1, 2, 3, None, 4]).main()
    res = s.tree2str(root)
    assert res == "1(2()(4))(3)"
