from collections import Counter

a = [1,2,3,5]
b = [2,3,4]
aa = Counter(a)
bb = Counter(b)
c = aa - bb
print(c)
print(sum(c.values()))
