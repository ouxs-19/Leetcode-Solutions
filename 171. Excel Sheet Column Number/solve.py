class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0 
        mul = 1
        for c in columnTitle[::-1]:
            res += (ord(c)-64)*mul
            mul *= 26
        
        return res