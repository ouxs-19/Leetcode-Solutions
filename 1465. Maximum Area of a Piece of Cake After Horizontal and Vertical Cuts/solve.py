class Solution(object):
    def maxArea(self, h, w, a, b):
        a.sort()
        b.sort()
        a.insert(0,0)
        b.insert(0,0)
        a.append(h)
        b.append(w)
        hs = 0
        ws = 0
        for i in range(1,len(a)):
            hs = max(hs,a[i]-a[i-1])
        for i in range(1,len(b)):
            ws = max(ws,b[i]-b[i-1])
        return hs*ws% (10**9 + 7)
