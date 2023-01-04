BS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(s, b):
            res = ""
            while s:
                res+=BS[s%b]
                s//= b
            return res[::-1] or "0"
            
        for i in range(2,n-1):
            res = to_base(n,i)
            if res != res[::-1]: return False 
        return True 