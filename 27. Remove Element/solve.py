class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        count = nums.count(val)
        i , j = 0 , k-1
        while i<j:
            if nums[i] == val :
                while j>i and nums[j] == val:
                    j-=1
                nums[i] , nums[j] = nums[j] , nums[i]
            i+=1
        return k-count
        