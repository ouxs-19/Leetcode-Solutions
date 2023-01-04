class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums)<3 : 
            return False 
        for i in range(len(nums)-2):
            s = nums[i]+nums[i+1]
            for j in range(i+1,len(nums)-1):
                if s == nums[j]+nums[j+1]: 
                    return True
        return False 