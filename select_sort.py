def select_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 45, 22, 39, 12, 55, 80]
    print(li)
    select_sort(li)
    print(li)
