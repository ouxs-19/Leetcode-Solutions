class Solution:
    def findOriginalArray(self, c: List[int]) -> List[int]:
        c.sort()
        res, need = [], defaultdict(int)
        verif = 0 
        for num in c : 
            if need[num]:
                need[num]-=1
                verif-=1
            else :
                need[2*num]+=1
                res.append(num)
                verif+=1
        if not verif : return res
        else : return []