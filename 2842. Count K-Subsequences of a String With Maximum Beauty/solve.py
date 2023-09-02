class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:       
        MOD = 1000000007
        beauty = Counter(s)
        beauty = list(beauty.values())
        beauty.sort(reverse=True)
        best_beauty = sum(beauty[:k])

        n = len(beauty)
        
        if k > 26 or k > n : return 0 

        @cache
        def custom_comb(i, j, curr):
            if i == n :
                if j == 0 and curr == best_beauty : return 1 
                return 0    
            return custom_comb(i+1, j, curr) + beauty[i]*custom_comb(i+1, j-1, curr+beauty[i])

        return custom_comb(0, k, 0) % MOD