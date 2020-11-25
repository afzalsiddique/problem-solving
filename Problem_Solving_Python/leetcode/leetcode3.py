class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0 or n==1:
            return n
        di = {}
        for char in s:
            di[char] = 0
        left, right = 0, 0
        maxx = 0
        di[s[left]]+=1
        while True:
            window = s[left:right-left+1]
            if right == n-1:
                maxx = max(maxx, right-left+1)
                break
            if di[s[right+1]] == 0:
                di[s[right+1]]+=1
                right+=1
                window = s[left:right-left+1]
                maxx = max(maxx, right-left+1)
                continue
            if left == right:
                di[s[left]]-=1
                di[s[right+1]]+=1
                left+=1
                right+=1
                window = s[left:right-left+1]
                maxx = max(maxx, right-left+1)
                continue
            if di[s[right+1]] == 1:
                di[s[left]]-=1
                left+=1
                window = s[left:right-left+1]
                maxx = max(maxx, right-left+1)
                continue
        return maxx
