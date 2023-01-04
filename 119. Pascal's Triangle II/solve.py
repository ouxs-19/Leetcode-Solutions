from math import comb
class Solution:
    def getRow(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(comb(n,i))
        return res