class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c[0]*c[1] for c in Counter(s).most_common())