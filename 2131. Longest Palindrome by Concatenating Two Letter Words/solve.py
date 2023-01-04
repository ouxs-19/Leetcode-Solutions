class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        c = False
        for word, i in count.items():
            if word[0] == word[1]:
                if i % 2 == 0:
                    res += i
                else:
                    res += i - 1
                    c = True
            elif word[0] < word[1]:
                res += 2 * min(i, count[word[1] + word[0]])
        if c:
            res += 1
        return 2 * res