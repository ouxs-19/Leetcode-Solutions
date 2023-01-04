class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        nums = sorted(set(nums))
        lc = 0 
        c = 0 
        lv = nums[0]-1
        for val in nums :
            if val == lv+1  :
                c+=1
            else:
                lc = max(c,lc)
                c = 1 
            lv = val 
        lc = max(c,lc)
        return lc 