class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def ksum(nums,k,target):
            res = []
            if not nums : 
                return res
            temp_target = target // k
            if temp_target<nums[0] or temp_target>nums[-1]:
                return res
            if k == 2 : 
                return twosum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for sub_res in ksum(nums[i+1:], k-1,target-nums[i]):
                        res.append([nums[i]]+sub_res)
            return res
        
        def twosum(nums,target):
            res = []
            l = len(nums)-1
            bi, bs = 0, l
            while bi<bs:
                curr = nums[bi]+nums[bs]
                if curr < target or bi>0 and nums[bi]==nums[bi-1]  : 
                    bi+=1
                elif curr > target or bs<l and nums[bs]==nums[bs+1]:
                    bs-=1
                else:
                    res.append([nums[bi],nums[bs]])
                    bi+=1
                    bs-=1
            return res
        return ksum(nums,4,target)