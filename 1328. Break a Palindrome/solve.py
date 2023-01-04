class Solution:
    def breakPalindrome(self, p: str) -> str:
        l = len(p)
        if l == 1 : return "" 
        ind = l//2
        impair = l%2
        s = [c for c in p]
        for i, char in enumerate(s):
            if char > "a":
                if impair and  i == ind :
                    continue
                s[i] = "a"
                break
        else :
            s[-1] = chr(ord(s[-1])+1)
        return "".join(s)
                