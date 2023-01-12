#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#
from typing import List

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        k_dict = {}
        for k in knowledge:
            k_dict[k[0]] = k[1]
        stack = []
        for i in s:
            if i == ")":
                tmp_str = ""
                while True:
                    top = stack.pop()
                    if top == "(":
                        stack.append(k_dict.get(tmp_str[::-1], "?"))
                        break
                    else:
                        tmp_str += top
            else:
                stack.append(i)
        return "".join(stack)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]])
    print(res)
    res = s.evaluate("hi(name)", [["a", "b"]])
    print(res)
