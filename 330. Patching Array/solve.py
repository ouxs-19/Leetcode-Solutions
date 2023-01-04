class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr, res , ind  = 0, 0, 0
        m = len(nums)
        while curr < n:
            if ind < m and nums[ind] <= curr + 1:
                curr += nums[ind]
                ind += 1
            else:
                res += 1
                curr = 2*curr + 1       
        return res