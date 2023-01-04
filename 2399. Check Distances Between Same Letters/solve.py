class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz"
        for char in a : 
            if char in s : 
                first= s.index(char)
                dist = s.index(char,first+1)-first-1
                if dist<0:dist=0
                if dist != distance[ord(char)-97]:
                    return False
        return True