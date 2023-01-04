class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a,b = Counter(r), Counter(m)
        for char in a : 
            if char not in b or a[char]>b[char]:
                return False
        return True