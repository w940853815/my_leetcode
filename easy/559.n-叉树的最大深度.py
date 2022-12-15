#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    max_dept = 0

    def maxDepth(self, root: "Node") -> int:
        # Time Limit Exceeded
        # if not root:
        #     return 0

        # def dfs(root, ans_dept=1):
        #     while root.children:
        #         ans_dept += 1
        #         for node in root.children:
        #             root = node
        #             dfs(node, ans_dept)
        #     self.max_dept = max(self.max_dept, ans_dept)
        #     return self.max_dept

        # return dfs(root)

        return (
            max((self.maxDepth(child) for child in root.children), default=0) + 1
            if root
            else 0
        )


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    n5 = Node(5)
    n6 = Node(6)
    n3 = Node(3, [n5, n6])
    n2 = Node(2)
    n4 = Node(4)
    root = Node(1, [n3, n2, n4])
    res = s.maxDepth(root)
    print(res)
