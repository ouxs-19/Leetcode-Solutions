from string import ascii_lowercase
from string import ascii_uppercase
class Solution:
    def makeGood(self, s: str) -> str:
        done = False
        while not done:
            done = True
            for c1,c2 in zip(ascii_lowercase,ascii_uppercase):
                cond = c1+c2
                if cond in s:
                    s = s.replace(cond,"")
                    done = False
                    
            for c2,c1 in zip(ascii_lowercase,ascii_uppercase):
                cond = c1+c2
                if cond in s:
                    s = s.replace(cond,"")
                    done = False

        return s