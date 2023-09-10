class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        used = set()
        for a,b in zip(s,t):
            if a in seen :
                if seen[a] != b : 
                    return False 
            else:
                if b in used: 
                    return False
                seen[a] = b
                used.add(b)

        return True