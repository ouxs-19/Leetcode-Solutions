from itertools import combinations

class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        for i in range(1,len(nums)+1):
            for comb in combinations(nums,i):
                l = sorted(list(comb))
                if l not in res :
                    res.append(l)
        return res
        