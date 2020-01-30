#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start


class Solution:
    def simplifyPath(self, path: str) -> str:
        # 思路不清晰，逻辑混乱，太复杂pass
        # stack_ = list()
        # for p in path:
        #     if len(stack_) == 0:
        #         stack_.append(p)
        #     # 先处理./ 和多个//问题
        #     # print(stack_[-1], p)
        #     if stack_[-1] == '/' and p == '/':
        #         continue
        #     if stack_[-1] == '.' and stack_[-2] != '.' and p == '/':
        #         stack_.pop()
        #         continue
        #     stack_.append(p)

        # # 处理../
        # res = list()

        # # print(''.join(stack_))
        # # res = ''.join(stack_)

        # for s in stack_:
        #     if len(res) >= 2:
        #         if res[-1] == '.' and res[-2] == '.' and s == '/':
        #             # pop /..
        #             res.pop()
        #             res.pop()
        #             res.pop()
        #             if len(res) > 0:
        #                 while res[-1] != '/':
        #                     res.pop()
        #                 # res.pop()
        #                 continue
        #     res.append(s)
        # # 最后以..结尾
        # if len(res) > 2:
        #     if res[-1] == '.' and res[-2] == '.':
        #         res.pop()
        #         res.pop()
        # # 最后一个目录名后面没有斜杠。
        # if res[-1] == '/' and len(res) > 1:
        #     res.pop()
        # # print(''.join(res))
        # return ''.join(res)
        stack = []
        path = path.split("/")
        # print(path)
        for item in path:
            if item == "..":
                if stack:
                    stack.pop()
            elif item and item != ".":
                stack.append(item)
        # print(stack)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    res = s.simplifyPath('/../')
    res = s.simplifyPath('/home//foo/')
    res = s.simplifyPath('/a/./b/../../c/')
    res = s.simplifyPath('/a/../../b/../c//.//')
    res = s.simplifyPath('/a//b////c/d//././/..')
    res = s.simplifyPath('/a//b////c/d//././/..')
    res = s.simplifyPath('/.')
    res = s.simplifyPath('/..')
    print(res)
# @lc code=end
