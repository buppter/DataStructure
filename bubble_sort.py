def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            return


if __name__ == "__main__":
    li = [54, 26, 93, 45, 22, 39, 12, 55, 80]
    print(li)
    bubble_sort(li)
    print(li)
