def poly_series(n):
    if n == 1:
        print("1", end=" ")
        return
    if n == 2:
        print("1 + x", end=" ")
        return
    poly_series(n - 1)
    print(" + x^", n - 1, end=" ")


poly_series(1)
print()
poly_series(2)
print()
poly_series(5)
