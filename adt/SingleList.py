
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleList:

    def __init__(self, Node=None):
        self._head = Node

    def is_empty(self):
        """是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        count = 0
        cur = self._head
        if self.is_empty():
            pass
        else:
            while cur:
                count += 1
                cur = cur.next
        return count

    def add(self, val):
        """头部插入"""
        node = Node(val)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def append(self, val):
        """尾部插入"""
        node = Node(val)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def travel(self):
        """遍历链表"""
        cur = self._head
        if self.is_empty():
            print('is empty')
            return
        while cur:
            print(cur.val, end=' ')
            cur = cur.next

    def remove(self, val):
        """删除指定元素"""
        if self.is_empty():
            return
        else:
            pre = self._head
            cur = self._head
            while cur:
                if cur.val == val:
                    if cur == self._head:
                        self._head = cur.next
                    else:
                        pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next

    def search(self, val):
        """查找指定元素,存在返回True"""
        if self.is_empty():
            return False
        else:
            cur = self._head
            while cur:
                if cur.val == val:
                    return True
                else:
                    cur = cur.next
            return False

    def insert(self, pos, val):
        """指定位置插入元素"""
        node = Node(val)
        if pos <= 0:
            self.add(val)
        elif pos >= self.length():
            self.append(val)
        else:
            count = 0
            pre = self._head
            cur = self._head
            while cur:
                count += 1
                if count == pos:
                    pre.next = node
                    node.next = cur
                else:
                    pre = cur
                    cur = cur.next


if __name__ == "__main__":
    singlelist = SingleList()
    print('test is_empty', singlelist.is_empty())  # True
    # append
    singlelist.append(1)
    singlelist.append(2)
    singlelist.travel()  # 1,2

    # length
    print(singlelist.length())

    # add
    singlelist.add(3)
    singlelist.travel()  # 3,1,2

    # search
    print('\n test search')
    print(singlelist.search(2))
    print(singlelist.search(4))

    # remove
    print('\nremove')
    singlelist.remove(3)  # 1,2
    singlelist.travel()

    # insert
    print('\ninsert')
    singlelist.insert(0, 1)
    singlelist.insert(2, 3)
    singlelist.insert(4, 3)

    singlelist.travel()
