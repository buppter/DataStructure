def heapify(alist, length, start):
    if start >= length:
        return
    lchild = 2 * start + 1
    rchild = 2 * start + 2
    max_index = start

    if lchild < length and alist[lchild] > alist[max_index]:
        max_index = lchild
    if rchild < length and alist[rchild] > alist[max_index]:
        max_index = rchild
    if max_index != start:
        alist[max_index], alist[start] = alist[start], alist[max_index]
        heapify(alist, length, max_index)


def build_heap(alist, length):
    last_node = length - 1
    last_node_parent = (last_node - 1) // 2
    for i in range(last_node_parent, -1, -1):
        heapify(alist, length, i)


def heap_sort(alist, length):
    build_heap(alist, length)
    for i in range(length - 1, -1, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heapify(alist, i, 0)


if __name__ == "__main__":
    alist = [5, 2, 9, 4, 13, 3, 10, 21, 18]
    print("原始list: %s" % alist)
    build_heap(alist, len(alist))
    print("build heap：%s" % alist)
    heap_sort(alist, len(alist))
    print("heap sort: %s" % alist)
