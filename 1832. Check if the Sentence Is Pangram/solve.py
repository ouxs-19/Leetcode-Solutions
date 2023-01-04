from string import ascii_lowercase as al
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for c in al :
            if c not in sentence : 
                return False
        return True