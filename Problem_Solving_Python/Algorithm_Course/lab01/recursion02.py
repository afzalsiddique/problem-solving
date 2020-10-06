def recursion02(arr, idx, n):
    if n % 2 and idx == n // 2:
        print(arr[idx], arr[idx])
        return
    if idx == n // 2:
        return
    print(arr[idx], arr[-idx - 1])
    recursion02(arr, idx + 1, n)


recursion02([1, 2, 3, 4], 0, 4)
print("\n")
recursion02([1, 2, 3, 4, 5], 0, 5)
