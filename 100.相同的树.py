#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    s = Solution()
    isSame = s.isSameTree(p,q)
    print(isSame)

