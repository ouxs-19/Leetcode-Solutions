class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 : return 0
        count = 0 
        for i in range(n-2):
            num = nums[i]
            Un = nums[i+1]
            r = Un-num
            stop = False 
            j = i+2
            while j < n and not stop : 
                if nums[j]-Un == r : 
                    Un = nums[j]
                    j+=1
                    count+=1
                else : stop = True 
        return count