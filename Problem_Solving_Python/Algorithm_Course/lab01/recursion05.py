def calculate_prev_polynomial(x, n):
    if n == 1:
        return 1
    return pow(x, n - 1) + calculate_prev_polynomial(x, n - 1)


print(calculate_prev_polynomial(2, 5))
