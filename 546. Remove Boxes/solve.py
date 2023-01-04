from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(maxsize=None)
        def sol(i,j,k):
            if i > j: 
                return 0
            places = [ind for ind in range(i+1, j+1) if boxes[ind] == boxes[i]]
            res = (k+1)**2 + sol(i+1,j,0)
            return max([res] + [sol(i+1, ind-1, 0) + sol(ind, j, k+1) for ind in places])   
            
        return sol(0,len(boxes)-1, 0)