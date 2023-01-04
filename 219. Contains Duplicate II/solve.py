class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        d = {}
        for i in range(l):
            if nums[i] in d : 
                if (i-d[nums[i]])<=k : 
                    return True
            d[nums[i]] = i
            
        return False