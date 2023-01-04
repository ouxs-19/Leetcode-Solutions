vowels =  { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0, len(s)-1
        s = [i for i in s]
        while i<j:
            if s[i] in vowels:
                while j>i and s[j] not in vowels:
                    j-=1
                if j>i : 
                    s[i], s[j] = s[j], s[i] 
                    j-=1
            i+=1
        return "".join(s)