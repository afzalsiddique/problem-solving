# def max_arr_util(arr, idx, n, current_max):
#     if idx == n - 2:
#         return min(arr[idx+1], current_max)
#     maxx = max(arr[idx],arr[idx+1])
#     return max(maxx, max_arr_util(arr, idx+1, n, maxx))
#
# def max_arr(arr):
#     return max_arr_util(arr, 0, len(arr), arr[0])
#
#
# # print(max_arr([1, 2, 3, 4]))
# # print(max_arr([4, 3, 2, 1]))
# print(max_arr([1, 4, 3, 2]))
