class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda elem : elem[0], reverse = True)
        new_pairs = [pairs[0]]
        
        for a, b in pairs[1:]:
            if new_pairs[-1][0] > b: 
                new_pairs.append([a, b])
        
        return len(new_pairs)