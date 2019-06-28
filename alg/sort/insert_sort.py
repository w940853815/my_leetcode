def insert_sort(alist: list)->list:
    """选择排序
    :param alist:待排序列表
    :return:
    """
    n = len(alist)
    for i in range(1, n):
        j = i
        while j>0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j=j-1
            else:
                break


if __name__ == "__main__":
    li = [2, 4, 8, 1, 20, 11, 32, 11, 7]
    print('sort before', li)
    insert_sort(li)
    print('sort after', li)

# 最优时间复杂度(n)
# 最差时间复杂度(n^2)
