class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d, res = {}, []
        for i, word in enumerate(words):
            d[word[::-1]] = i
        for i, word in enumerate(words):
            if word in d and d[word] != i:
                res.append([i, d[word]])
            if word != "" and "" in d and word == word[::-1]:
                res.append([i, d[""]])
                res.append([d[""], i])
            for j in range(len(word)):
                if word[j:] in d and word[:j] == word[j-1::-1]:
                    res.append([d[word[j:]], i])
                if word[:j] in d and word[j:] == word[:j-1:-1]:
                    res.append([i, d[word[:j]]])
        return res