class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def check_right(nums,i,j):
            while i < j and nums[i]> 0 :
                i+=1
            i+=1
            return j-i+1

        def check_left(nums,i,j):
            while i < j and nums[j]> 0 :
                j-=1
            j-=1
            return j-i+1
        i ,j ,n = 0 , 0 , len(nums) 
        longest = 0
        while i < n :
            negs = 0 
            while j < n and nums[j]!= 0 :
                if nums[j] < 0 : 
                    negs += 1
                j+=1
            if  j == n or nums[j] == 0  : j-=1
            if negs % 2 == 0 : longest = max(longest,j-i+1) 
            else : 
                longest = max(longest,max(check_right(nums,i,j),check_left(nums,i,j)))
            if j == n-1 or nums[j+1] == 0 :
                j+=1
            j+=1
            i = j
        return longest

