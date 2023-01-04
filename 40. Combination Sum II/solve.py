class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = set()
        l = len(candidates)-1
        candidates.sort()
        n = len(candidates)
        self.cond = []
        def solve(curr,i):
            if curr == target :
                return self.results.add(tuple(self.cond.copy()))
            if i == n :  return 
            elif curr > target :
                return 
            self.cond.append(candidates[i])
            solve(curr+candidates[i],i+1)
            c = self.cond.pop()
            while i<l and candidates[i+1] == c : 
                i+=1
            solve(curr,i+1)
        solve(0,0)
        return self.results