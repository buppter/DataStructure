def binary_search(alist, item):
    """二分查找,递归方法"""
    n = len(alist)

    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search1(alist, item):
    """非递归，二分查找"""
    n = len(alist)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == "__main__":
    li = [12, 20, 22, 26, 39, 45, 54, 55, 80, 93]
    print(li)
    result = binary_search1(li, 55)
    print(result)
