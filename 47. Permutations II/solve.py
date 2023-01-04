import itertools
class Solution(object):
    def permuteUnique(self, nums):
        return list(set(itertools.permutations(nums)))
                
        