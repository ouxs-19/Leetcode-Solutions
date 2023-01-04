class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bi = 0 
        bs = len(nums)-1
        while bi <= bs :
            i = (bi + bs) //2
            if nums[i] == target : 
                return i 
            elif nums[i] > target :
                bs = i-1
            else :
                bi = i+1
        return bi