def find_util(arr, idx, n, q):
    if idx == n:
        return "not found"
    if arr[idx] == q:
        return idx
    return find_util(arr, idx + 1, n, q)


def find(n, arr, q, queries):
    for q in queries:
        print(find_util(arr, 0, n, q))


find(5, [2, 9, 4, 7, 6], 2, [5, 9])
