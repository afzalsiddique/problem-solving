def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    first = merge_sort(arr[:len(arr) // 2])
    second = merge_sort(arr[len(arr) // 2:])
    li = []
    i, j = 0, 0
    while i != len(first) or j != len(second):
        if first[i] <= second[j]:
            li.append(first[i])
            i += 1
        else:
            li.append(second[j])
            j += 1
        if i == len(first):
            li += second[j:]
            break
        if j == len(second):
            li += first[i:]
            break
    return li

# def is_less_than_or_equal(a, b):
    
