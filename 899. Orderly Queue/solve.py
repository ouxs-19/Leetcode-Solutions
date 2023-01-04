class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1 : 
            return "".join(sorted(s))
        best = s
        for i in range(1,len(s)):
            tmp = s[i:]+s[:i]
            if tmp < best : 
                best = tmp
        return best 