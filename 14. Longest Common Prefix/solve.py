class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs,key=len)
        n, m = len(strs), len(strs[0])
        if n == 1 : strs[0]
        i = 0
        prefix = ""
        while i < m :
            cond = strs[0][i]
            for word in strs[1:]:
                if word[i] != cond :
                    return prefix 
            prefix+=cond 
            i+=1
        return prefix