class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for r in matrix : 
            l.extend(r)
        l.sort()
        return l[k-1]