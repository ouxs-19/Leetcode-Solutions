class Solution(object):
    def firstMissingPositive(self, nums):
        nums = sorted(x for x in nums if x>0)
        try :
            if nums[0] != 1 :
                return 1
        except :
            return 1 
        
        last = nums[0]
        ind = 1
        n = len(nums)
        while ind < n:
            num = nums[ind]
            if num > 0 :
                if num-last > 1:
                    return last+1
                else :
                    last = num
            ind+=1
        return last+1
        