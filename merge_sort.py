def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    return merge(left_li, right_li)


def merge(left_li, right_li):
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_li) and right_point < len(right_li):
        if left_li[left_point] < right_li[right_point]:
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1
    result += left_li[left_point:]
    result += right_li[right_point:]
    return result


if __name__ == "__main__":
    li = [54, 26, 93, 45, 22, 39, 12, 55, 80, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)
