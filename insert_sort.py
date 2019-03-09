def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # i = j
        # i表示内层循环起始值
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        for i in range(j, 0, -1):
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break


if __name__ == "__main__":
    li = [54, 26, 93, 45, 22, 39, 12, 55, 80]
    print(li)
    insert_sort(li)
    print(li)
