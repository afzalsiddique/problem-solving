def remove_odd_util(arr, idx):
    if idx == len(arr):
        return arr
    if arr[idx] % 2:
        arr.pop(idx)
        return remove_odd_util(arr, idx)
    return remove_odd_util(arr, idx + 1)


def remove_odd(arr):
    return remove_odd_util(arr, 0)


print(remove_odd([1, 2, 3]))
print(remove_odd([1, 2, 3, 3, 3, 4, 5, 6]))
print(remove_odd([3]))
