class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = defaultdict(str)
        s = s.split()
        if len(s) != len(pattern) : return False
        seen = set()
        for c,w in zip(pattern,s):
            if d[c]:
                if d[c] != w : 
                    return False
            else :
                if w not in seen:
                    d[c] = w
                    seen.add(w)
                else :
                    return False
        return True