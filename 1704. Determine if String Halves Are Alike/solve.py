vowels = 'aeuio'
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a,b = s[:len(s)//2], s[len(s)//2:]
        print(a,b)
        return sum(a.count(c) for c in vowels) == sum(b.count(c) for c in vowels)
