class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0 : return 0  
        last = nums[0]
        i, k, ind = 1, n, 1

        while i < n :
            while i < n and nums[i] == last   :
                i+=1
                k-=1
            if i == n : 
                return k 
            last = nums[i]
            nums[ind] = last
            ind+=1
            i+=1
        return k