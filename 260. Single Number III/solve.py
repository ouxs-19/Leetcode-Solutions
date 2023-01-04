from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l = Counter(nums)
        return([i for i in l if l[i]==1])