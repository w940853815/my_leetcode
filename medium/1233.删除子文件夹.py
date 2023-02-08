#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#
from typing import List


# @lc code=start
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class Trie:
            def __init__(self) -> None:
                self.child = {}
                self.ref = -1

        # 超时
        # res = []
        # for index, i in enumerate(folder):
        #     for j in folder[index:]:
        #         if i in ["/", ""] or j in ["/", ""] or i == j:
        #             continue
        #         if i.find(j) == 0 and "/" in i.replace(j, ""):
        #             res.append(i)
        #         if j.find(i) == 0 and "/" in j.replace(i, ""):
        #             res.append(j)
        # return list(set((set(folder) - set(res))))
        root = Trie()
        for i, f in enumerate(folder):
            path = f.split("/")
            cur = root
            for name in path:
                if name not in cur.child:
                    cur.child[name] = Trie()
                cur = cur.child[name]
            cur.ref = i
        res = []

        def dfs(cur):
            if cur.ref != -1:
                res.append(folder[cur.ref])
                return
            for child in cur.child.values():
                dfs(child)

        dfs(root)
        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    print(res)
    # ["/a/b/c","/a/b/ca","/a/b/d"]
    res = s.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])
    print(res)
