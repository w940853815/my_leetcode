# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        return self.isInclude(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isInclude(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.isInclude(A.left, B.left) and self.isInclude(A.right, B.right)
