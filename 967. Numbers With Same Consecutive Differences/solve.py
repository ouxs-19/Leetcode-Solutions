class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.sol = []
        def solve(last,num,i):
            if i == n : 
                return self.sol.append(num)
            if k > 4 : 
                if last > 4 : 
                    if last-k > -1 : 
                        solve(last-k,num*10+last-k,i+1)
                else : 
                    if last+k < 10 : 
                        solve(last+k,num*10+last+k,i+1)
            else :
                for j in range(10):
                    if abs(j-last) == k : 
                        solve(j,num*10+j,i+1)
        for t in range(1,10):
            solve(t,t,1)
        return self.sol