# 定义节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


# 传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res