class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def construct(word, i):
            if word == s1 : return True 
            if i >= 2 : 
                return False
            chars = [c for c in word]
            chars[i], chars[i+2] = chars[i+2], chars[i]
            new_word = "".join(chars)
            return construct(word,i+1) or construct(new_word, i+1)
        
        return construct(s2,0)
        