class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ["a"]*n
        k = k-n
        ind = n-1
        if k == 0 : return "".join(s) 
        while k >= 26: 
            s[ind] = "z"    
            k = k-26+1
            ind-=1
        if k == 0 : return "".join(s) 
        s[ind] = chr(k+97)
        return "".join(s)