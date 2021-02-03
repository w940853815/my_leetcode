#
# @lc app=leetcode.cn id=1115 lang=python3
#
# [1115] 交替打印FooBar
#
# https://leetcode-cn.com/problems/print-foobar-alternately/description/
#
# concurrency
# Medium (55.53%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    29.2K
# Total Submissions: 52.6K
# Testcase Example:  '1'
#
# 我们提供一个类：
#
#
# class FooBar {
# ⁠ public void foo() {
# for (int i = 0; i < n; i++) {
# print("foo");
# }
# ⁠ }
#
# ⁠ public void bar() {
# for (int i = 0; i < n; i++) {
# print("bar");
# }
# ⁠ }
# }
#
#
# 两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
#
# 请设计修改程序，以确保 "foobar" 被输出 n 次。
#
#
#
# 示例 1:
#
#
# 输入: n = 1
# 输出: "foobar"
# 解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
#
#
# 示例 2:
#
#
# 输入: n = 2
# 输出: "foobarfoobar"
# 解释: "foobar" 将被输出两次。
#
#
#

# @lc code=start
from threading import Lock, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.flock = Lock()
        self.block = Lock()
        self.block.acquire()
        # self.flock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.flock.acquire()
            printFoo()
            self.block.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):

            # printBar() outputs "bar". Do not change or remove this line.
            self.block.acquire()
            printBar()
            self.flock.release()
# @lc code=end


def printFoo():
    print("foo")


def printBar():
    print("bar")


if __name__ == '__main__':
    s = FooBar(2)

    t1 = Thread(target=s.foo, args=(printFoo,))
    t2 = Thread(target=s.bar, args=(printBar,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
