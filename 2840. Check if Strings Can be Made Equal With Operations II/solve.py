class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        even_s1 = defaultdict(int)
        even_s2 = defaultdict(int)
        odd_s1 = defaultdict(int)
        odd_s2 = defaultdict(int)
        
        for i in range(0,n,2):
            even_s1[s1[i]]+=1
        
        for i in range(1,n,2):
            odd_s1[s1[i]]+=1

        for i in range(0,n,2):
            even_s2[s2[i]]+=1
        
        for i in range(1,n,2):
            odd_s2[s2[i]]+=1
        
        for char in even_s1:
            if even_s1[char] != even_s2[char] : return False
        for char in odd_s1:
            if odd_s1[char] != odd_s2[char] : return False
        
        return True