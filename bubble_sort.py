def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1, 0, -1):
        for i in range(0, n-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]




