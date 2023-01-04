class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def custom(w) : 
            ind = -1
            for char in w : 
                ind = s.find(char, ind+1)
                if ind == -1 : return 0
            return True 
        return sum(map(custom, words))
        