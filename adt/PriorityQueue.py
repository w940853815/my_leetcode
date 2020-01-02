# 实现一个优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.index = 0
    # 队列包含了一个 (-priority, index, item) 的元组。优先级为负 数的目的是使得元素按照优先级从高到低排序。这个跟普通的按优先级从低到高排序 的堆排序恰巧相反。

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        heapq.heappop(self._queue)

    def __repr__(self):
        return str(self._queue)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push('23123', 4)
    pq.push('23123', 5)
    print(pq)
    pq.pop()
    print(pq)
