class Solution(object):
    def findLUSlength(self, strs):
        def check(cond,t):
            t = iter(t)
            return all(char in t for char in cond)
 
        strs.sort(key = lambda x:-len(x))
        for i, cond in enumerate(strs):
            if all(not check(cond, strs[j]) for j in range(len(strs)) if j != i): 
                return len(cond)
        return -1