class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0 : return 1
        if n == 0 : return 0 
        count = [1] + [0 for i in range(k)]
        for i in range(1, n):
            new = [1] + [0 for _ in range(k)]
            inverse = 1 
            for j in range(1, k+1):
                inverse += count[j]
                if j >= i+1: inverse -= count[j-i-1] 
                new[j] = inverse
            count = new
        return count[-1] % 1000000007