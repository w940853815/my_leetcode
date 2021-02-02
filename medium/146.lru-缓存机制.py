#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.52%)
# Likes:    1129
# Dislikes: 0
# Total Accepted:    128K
# Total Submissions: 248.2K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
#
#
#
# 实现 LRUCache 类：
#
#
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#
#
#
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
# 提示：
#
#
# 1
# 0
# 0
# 最多调用 3 * 10^4 次 get 和 put
#
#
#

# @lc code=start


class DLinkNode:
    def __init__(self, key=0, val=0) -> None:
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # 使用伪头部节点和伪尾部节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # 如果存在，则返回结果，并将节点移到头部
            node = self.cache[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果不存在，创建一个新的节点，并移到头部
            node = DLinkNode(key, value)
            self.addHead(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                # 超出容量后，删除尾部节点
                remove = self.removeTail()
                self.cache.pop(remove.key)
                self.size -= 1
        else:
            # 如果key存在，则替换val，并移到头部
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addHead(node)

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node

    def addHead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
