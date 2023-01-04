class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1 : return s 
        m = len(s)
        final = ""
        for i in  range(0,m,2*n-2):
            final+=s[i]
        for i in range(1,n-1):
            for j  in range(i,m,2*n-2):
                k = j+2*(n-i-1)
                final+=s[j]
                if k<m : 
                    final+=s[k]
        for i  in range(n-1,m,2*n-2):
            final+=s[i]  
        return final