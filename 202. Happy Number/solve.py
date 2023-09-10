class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen: return False
            if n == 1 : return True
            seen.add(n)
            n = sum([int(c)**2 for c in str(n)])  