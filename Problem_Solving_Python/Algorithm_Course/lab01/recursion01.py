def reverse_print(idx, arr):
    if idx == len(arr):
        return
    reverse_print(idx + 1, arr)
    print(arr[idx], end=" ")
reverse_print(0, [1,2,3,4])
