class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) -1 
        if n == 0 : return True 
        i = n 
        possible = True 
        while i >= 0 :
            if nums[i] == 0 :
                possible = False
                k = 1-1*(i==n) 
                i-=1
                while i >=0 and not possible :
                    if nums[i] > k : 
                        possible = True 
                    else :
                        i-=1
                        k+=1
            else :
                i-=1 
        return possible 