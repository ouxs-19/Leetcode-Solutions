class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r = 1
        r_r = 1
        n = len(nums)
        left_muls = {0:1}
        right_muls = {n-1:1}
        for i in range(n-1) :
            l_r*=nums[i]
            r_r*=nums[n-i-1]
            right_muls[n-i-2] = r_r
            left_muls[i+1] = l_r 
        res = []
        for i in range(n):
            res.append(left_muls[i]*right_muls[i])
        return res