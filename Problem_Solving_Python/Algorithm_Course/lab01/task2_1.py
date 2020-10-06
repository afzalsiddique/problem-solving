def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    first = merge_sort(arr[:len(arr) // 2])
    second = merge_sort(arr[len(arr) // 2:])
    sorted_array = []
    i, j = 0, 0
    while i != len(first) or j != len(second):
        if first[i] <= second[j]:
            sorted_array.append(first[i])
            i += 1
        else:
            sorted_array.append(second[j])
            j += 1
        if i == len(first):
            sorted_array += second[j:]
            break
        if j == len(second):
            sorted_array += first[i:]
            break
    return sorted_array


def find_median(arr):
    n = len(arr)
    arr = merge_sort(arr)
    if n % 2:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) // 2

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    print(find_median(arr))



