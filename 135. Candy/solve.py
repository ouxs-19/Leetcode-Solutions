class Solution:
    def candy(self, pri: List[int]) -> int:
        ln = len(pri)
        l,r = [1]*ln, [1]*ln  
        for i in range(1,ln):
            if pri[i] > pri[i-1]:
                l[i] = l[i-1]+1
        for i in range(ln-2,-1,-1):
            if pri[i] > pri[i+1] :
                r[i] = r[i+1]+1
        for i in range(ln):
            l[i] = max(l[i], r[i])
        return sum(l)
