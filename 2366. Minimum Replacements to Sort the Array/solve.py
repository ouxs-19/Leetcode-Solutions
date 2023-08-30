class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        cnt = 0 

        for i in range(ln-2, -1, -1):
            if nums[i] > nums[i+1]:
                res = ( nums[i] + nums[i+1] -1 ) // nums[i+1]
                cnt += res -1
                nums[i] = nums[i] // res 
                
        return cnt 