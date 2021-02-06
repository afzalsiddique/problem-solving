def f(n):
    weeks = n //7
    temp = n % 7
    cnt = 0
    if temp == 0:
        cnt = 0
    elif temp == 1:
        cnt = 1
    elif temp == 2:
        cnt = 2
    elif temp == 3:
        cnt = 3
    elif temp == 4:
        cnt = 5
    elif temp == 5:
        cnt = 7
    elif temp == 6:
        cnt = 8
    return weeks * 9 + cnt

for _ in range(int(input())):
    print(f(int(input())))
