class Solution:
    def countAndSay(self, n: int) -> str:
        def say(s):
            last = s[0]
            n = len(s)
            res = ""
            cnt = 1 
            i = 1 
            written = False 
            while i < n : 
                while i < n and s[i] == last :
                    cnt+=1
                    i+=1
                res+=str(cnt)+last
                written = True 
                if i < n : 
                    cnt = 1
                    last = s[i]
                    i+=1
                    written = False 
            if not written : 
                res+=str(cnt)+last
            
            return res
        
        def solve(i):
            if i == 1 : 
                return "1"
            return say(solve(i-1))
        
        return solve(n)