class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        first_arr = nums[:k]
        dic = defaultdict(int)
        dist = 0
        sm = 0
        best = 0
        n = len(nums)
        last = 0
        for i in range(k):
            dic[nums[i]]+=1
            sm += nums[i]
            if dic[nums[i]] == 1 : dist +=1 
        if dist >= m:  
            best = sm 
            
        for j in range(k,n):
            dic[nums[last]] -= 1 
            if dic[nums[last]] == 0 : dist -=1 
            dic[nums[j]] += 1 
            if dic[nums[j]] == 1 : dist +=1 

            sm -= nums[last]
            sm += nums[j]            
            if dist >= m : best = max(best,sm)
            last+=1
            
        return best