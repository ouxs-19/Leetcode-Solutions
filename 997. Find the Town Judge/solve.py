class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [i for i in range(1,n+1)]
        trusts = defaultdict(set)
        for tr in trust:
            if tr[0] in trusting:
                 trusting.remove(tr[0])
            trusts[tr[1]].add(tr[0])
        
        for cond in trusting :
            if len(trusts[cond]) == n-1 : 
                return cond
        return -1