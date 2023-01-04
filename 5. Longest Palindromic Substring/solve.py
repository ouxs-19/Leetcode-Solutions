class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for i in range(length,0,-1):
            for j in range(length-i,-1,-1):
                ss = s[j:j+i]
                if ss == ss[::-1]:
                    return ss