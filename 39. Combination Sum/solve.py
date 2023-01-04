class Solution(object):
    def combinationSum(self, candidates, target):
        self.results = []
        n = len(candidates)
        self.cond = []
        def solve(curr,i):
            if i == n :  return 
            if curr == target :
                return self.results.append(self.cond.copy())
            
            elif curr > target :
                return 
            self.cond.append(candidates[i])
            solve(curr+candidates[i],i)
            self.cond.pop()
            solve(curr,i+1)
        solve(0,0)
        return self.results