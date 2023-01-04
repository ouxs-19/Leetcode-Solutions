class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops :
            n,m = map(min,zip(*ops))
        return n*m