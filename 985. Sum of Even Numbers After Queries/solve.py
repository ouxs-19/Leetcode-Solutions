class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        last = sum(i for i in nums if not i%2)
        for q in queries : 
            add, i = q
            is_odd = add % 2 
            if nums[i] % 2 : 
                if is_odd:
                   last = last+nums[i]+add
            else :
                if is_odd:
                    last-=nums[i]
                else:
                   last+=add
            nums[i]+=add
            res.append(last)
        return res