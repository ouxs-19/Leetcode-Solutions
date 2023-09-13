class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0 
        for snt in sentences:
            mx = max(mx, len(snt.split()))
        
        return mx