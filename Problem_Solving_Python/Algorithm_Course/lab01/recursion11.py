def max_arr_util(arr, idx, n):
    if idx == n - 1:
        return arr[idx]
    return max(arr[idx], max_arr_util(arr, idx + 1, n))


def max_arr(arr):
    return max_arr_util(arr, 0, len(arr))


print(max_arr([1, 2, 3, 4]))
print(max_arr([4, 3, 2, 1]))
print(max_arr([1, 4, 3, 2]))
