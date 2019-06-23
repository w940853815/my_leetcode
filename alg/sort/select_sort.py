def select_sort(alist: list)->list:
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]


if __name__ == "__main__":
    li = [2, 4, 8, 1, 20, 11, 32, 11, 7]
    print('sort before', li)
    select_sort(li)
    print('sort after', li)

# 最优时间复杂度（n^2）
# 最坏时间复杂度（n^2）
