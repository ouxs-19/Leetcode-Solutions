from numpy import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def check_right(nums,i,j):
            if i == j : return nums[i]
            while i < j and nums[i]> 0 :
                i+=1
            i+=1
            if i == j : return nums[i]
            return prod(nums[i:j+1])
        def check_left(nums,i,j):
            while i < j and nums[j]> 0 :
                j-=1
            if i == j : return nums[i]
            return prod(nums[i:j])
        
        if not any(nums) : return 0
        i ,j ,n = 0 , 0 , len(nums) 
        longest = float("-inf")
        while i < n :
            negs = 0 
            while j < n and nums[j]!= 0 :
                if nums[j] < 0 : 
                    negs += 1
                j+=1
            if  j == n or nums[j] == 0  : j-=1
            if negs % 2 == 0 : 
                if j < i : 
                    longest = max(longest,0) 
                else : 
                    longest = max(longest,prod(nums[i:j+1])) 
            else : 
                longest = max(longest,max(check_right(nums,i,j),check_left(nums,i,j)))
            if j == n-1 or nums[j+1] == 0 :
                j+=1
            j+=1
            i = j
        return int(max(longest,max(nums)))