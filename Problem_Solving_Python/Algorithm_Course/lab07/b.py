def get_cnt(string):
    n = len(string)
    z = [0]*n

    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:

            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:

                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    cnt = 0
    for i in range(n):
        if z[i] + i == n:
            cnt+=1
    return cnt


for case in range(int(input())):
    print("Case {}: {}".format(case+1, get_cnt(input())))


