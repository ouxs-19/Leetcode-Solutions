class Solution:
    def countSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        c = len(s)
        for i in range(len(s)):
            d[(i,i)] = 1
        for l in range(1,len(s)):
            for i in range(len(s)-l):
                j = i+l
                x,y = i+1,j-1
                if s[i] == s[j] and (d[(x,y)] or x>y):
                    c+=1
                    d[(i,j)] = 1
        return c