class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def isnice(arr,num):
            for n in arr :
                if n & num : 
                    return False
            return True
        i,mx = 1,1
        n = len(nums)
        r = [nums[0]]
        while i < n:
            if isnice(r,nums[i]):
                r.append(nums[i])
                mx = max(mx,len(r))
                i+=1
            else:
                r.pop(0)   
        return mx