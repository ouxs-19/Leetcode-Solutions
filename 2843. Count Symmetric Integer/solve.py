class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0 
        for i in range(low,high+1):
            s = str(i)
            n = len(s) 
            if n%2 == 0 :
                h1, h2 = s[:n//2], s[n//2:]
                if sum(map(int,h1)) == sum(map(int,h2)):
                    cnt+=1
        return cnt