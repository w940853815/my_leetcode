#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#

# @lc code=start
class BrowserHistory:
    def __init__(self, homepage: str):
        self.his = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        del self.his[self.index + 1 :]
        self.his.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.his[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.his) - 1, self.index + steps)
        return self.his[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
