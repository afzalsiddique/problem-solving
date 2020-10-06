def merge_sort(tuple_list):
    if len(tuple_list) == 1:
        return tuple_list
    if len(tuple_list) == 2:
        if tuple_list[0] > tuple_list[1]:
            tuple_list[0], tuple_list[1] = tuple_list[1], tuple_list[0]
        return tuple_list
    first = merge_sort(tuple_list[:len(tuple_list) // 2])
    second = merge_sort(tuple_list[len(tuple_list) // 2:])
    sorted_array = []
    i, j = 0, 0
    while i != len(first) or j != len(second):
        if is_less_than_or_equal(first[i], second[j]):
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


def is_less_than_or_equal(a, b):
    if a[0] < b[0]:
        return True
    elif a[0] == b[0]:
        if a[1] <= b[1]:
            return True
        else:
            return False
    elif a[0] > b[0]:
        return False


def generate_tuples(arr):
    tuple_list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            tuple_list.append((arr[i], arr[j]))
    return tuple_list


def final(arr, k):
    tuple_list = generate_tuples(arr)
    sorted_array = merge_sort(tuple_list)
    return sorted_array[k - 1]


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = final(arr, k)
print(result[0], result[1])