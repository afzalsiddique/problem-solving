import itertools
from operator import mul, add


sett = set()
dp={}
def helper(src,tar):
    if src == tar: return 0
    if src in sett: return float('inf')
    sett.add(src)
    if src in dp: return dp[src]
    source=list(src)
    res = float('inf')
    for i in range(len(src)-1):
        source[i],source[i+1]=source[i+1],source[i]
        temp = helper(''.join(source),tar)
        res = min(res,1+temp)
        source[i],source[i+1]=source[i+1],source[i]
    dp[src]=res
    return res

print(helper('11112','21111'))
src,tar="5489355142","5489355421"
print(helper(src[::-1],tar[::-1]))