class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        dic = {}
        i = 0 
        for num in nums :
            dic[num] = i
            i+=1

        seen = set()
        ind = 0 
        for numm in nums : 
            if numm not in seen :
                seen.add(numm)
                target = -numm
                treated = set()
                for k in range(ind+1,len(nums)):
                    num = nums[k]
                    if num not in treated : 
                        treated.add(num)
                        s = target - num 
                        if s in dic and k!=dic[s] and k!=ind and dic[s]!=k and dic[s]!=ind and dic[s]>k>ind:
                            res.append([numm,num,s])
            ind+=1
        return res