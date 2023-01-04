class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums :
            r = nums.index(target)
            nums.reverse()
            return [r,len(nums)-1-nums.index(target)]
        return [-1,-1]