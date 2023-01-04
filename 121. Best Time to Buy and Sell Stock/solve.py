class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        minprice , bestprofit = nums[0] , 0 
        while i < n-1 :
            while i < n -1 and nums[i]>= nums[i+1]:
                i+=1
            temp_min = nums[i]
            while i < n -1 and nums[i]<= nums[i+1]:
                i+=1
            minprice = min(minprice,temp_min)
            profit = nums[i]-minprice
            bestprofit = max(bestprofit,profit)
        return bestprofit