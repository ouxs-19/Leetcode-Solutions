class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = collections.Counter(sorted(arr,key=abs))
        if 0 in dic :
            if dic[0]%2 == 1 :return False 
            dic.pop(0)
        for num in dic :
            v = dic[num]
            dic[num] = 0 
            if v > 0 :
                s = num*2
                if s not in dic :
                    return False
                dic[s]= dic[s]-v
                if dic[s] <0 : return False 
        return True