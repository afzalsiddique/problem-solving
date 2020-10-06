def reverse_string_util(my_str, idx, n):
    if idx == n:
        return ""
    return reverse_string_util(my_str, idx + 1, n) + my_str[idx]


def reverse_string(my_str):
    return reverse_string_util(my_str, 0, len(my_str))


print(reverse_string("abcd"))
