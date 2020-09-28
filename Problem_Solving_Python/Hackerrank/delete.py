li = map(int, input().split())
li = list(li)
li = [[li[i],li[i+1]] for i in range(0, len(li),2)]
print(li)