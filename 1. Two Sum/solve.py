class Solution(object):
    def twoSum(self, nums, target):
        i = 0 
        dic = {}
        while i < len(nums) :
            dic[nums[i]] = i
            i+=1

        i = 0
        
        for num in nums :
            s = target - num 
            if s in dic and i!=dic[s] :
                return [i,dic[s]]
            i+=1