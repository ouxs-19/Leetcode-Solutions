class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = set()
        dik = []
        for num in nums :
            if num not in dic : 
                dic.add(num)
            else :
                dik.append(num)
        return dik