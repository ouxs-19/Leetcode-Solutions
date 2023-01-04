class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def solve(word):
            dic1, dic2 = {}, {}
            for a, b in zip(word, pattern):
                if a not in dic1: dic1[a] = b
                if b not in dic2: dic2[b] = a
                if (dic1[a], dic2[b]) != (b, a):
                    return False
            return True
        l = []
        for w in words : 
            if solve(w):
                l.append(w)
        return l