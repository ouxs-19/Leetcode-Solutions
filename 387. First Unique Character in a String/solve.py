class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = set()
        for i, char in enumerate(s):
            if char not in chars and  s[i+1:].find(char) == -1 : 
                return i
            chars.add(char)
        return -1 
            