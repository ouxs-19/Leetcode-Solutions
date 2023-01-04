class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i,j = 0, len(tokens)-1
        res, best = 0, 0  
        while i<j : 
            if power >= tokens[i]:
                res+=1
                power-=tokens[i]
                i+=1
            else :
                power += tokens[j]
                res-=1
                j-=1

            best = max(best,res)
            if res < 0 : return 0 
        if i == j and power >= tokens[i] : 
            res += 1
            best = max(best,res)
        return best 