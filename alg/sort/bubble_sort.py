def bubble_sort(alist: list)->list:
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def bubble_sort_pro(alist: list)->list:
    """冒泡排序改进"""
    n = len(alist)
    for j in range(0, n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            # 没发生交换，说明0~n-1-j间都有序，后面不需要排序了
            break


if __name__ == "__main__":
    li = [2, 4, 8, 1, 20, 11, 32, 11, 7]
    print('sort before', li)
    bubble_sort_pro(li)
    print('sort after', li)
