class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return [c for c in "".join(word1)] == [c for c in "".join(word2)]