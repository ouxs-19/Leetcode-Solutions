class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        bestprofit = 0 
        while i < n-1 :
            while i < n -1 and nums[i]>= nums[i+1]:
                i+=1
            minprice = nums[i]
            while i < n -1 and nums[i]<= nums[i+1]:
                i+=1
            bestprofit += nums[i]-minprice
        return bestprofit