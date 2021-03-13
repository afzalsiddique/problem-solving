# code from gfg
def computeLPSArray( pat):
    leng = 0 # length of the previous longest prefix suffix
    i=1
    m = len(pat)
    lps=[0]*m
    while i < m:
        if pat[i]== pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1] # go back to previous longest prefix suffix
            else:
                lps[i] = 0
                i += 1
    return lps

# run this to understand lps
print(computeLPSArray("aaaabaabd"))


def kmp(text: str, pattern: str) -> int:
    m,n= len(text), len(pattern)
    if n==0:return 0
    if m==0:return -1
    i,j=0,0
    lps = computeLPSArray(pattern)
    while i<m:
        if text[i]==pattern[j]:
            i+=1
            j+=1
        if j==n:
            return i-j
        if i<m and pattern[j]!=text[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return -1
# run this to understand kmp
print(kmp('ababcabcabababd', 'ababd'))
