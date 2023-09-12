class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = Counter(s)
        seen  = set()
        cnt   = 0

        for freq in freqs.values():
            while freq > 0 and freq in seen:
                freq -= 1 
                cnt  += 1
            
            seen.add(freq)

        return cnt