class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = Counter(nums)
        res = []
        k = 0 
        for i in range(1,n+1):
            if c[i] > 1 : 
                res.insert(k,i)
                k+=1
            if not c[i]:
                res.append(i)
        return res