def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    mid_value = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1

        alist[low] = alist[high]
        # low += 1

        while low < high and alist[low] < mid_value:
            low += 1

        alist[high] = alist[low]
        # high -= 1

    alist[low] = mid_value

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


if __name__ == "__main__":
    li = [54, 26, 93, 45, 22, 39, 12, 55, 80]
    print(li)
    quick_sort(li, 0, 8)
    print(li)
