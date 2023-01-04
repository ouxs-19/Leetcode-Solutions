class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        lower = float("inf")
        for i in range(len(nums)-2):
            while i > 0 and i < l-2 and nums[i] == nums[i-1]:
                i+=1
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target-lower) > abs(target-s):
                    lower = s
                if s < target:
                    l +=1 
                elif s > target:
                    r -= 1
                else:
                    return target
        return lower