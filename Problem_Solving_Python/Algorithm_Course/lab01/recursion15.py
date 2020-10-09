def reverse(n, current_sum):
    if n % 10 == n:
        return current_sum * 10 + n
    current_sum = current_sum * 10 + (n % 10)
    return reverse(n // 10, current_sum)

print(reverse(12345, 0))