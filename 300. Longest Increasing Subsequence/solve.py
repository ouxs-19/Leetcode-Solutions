class Solution:
    def lengthOfLIS(self, l: List[int]) -> int:
        n = len(l)
        ll = [1]+[0]*(n-1)
        i =1 
        while i < n :
            j = i-1
            add = 0 
            while j >= 0 :
                if l[j] < l[i] :
                    add = max(add,ll[j])
                j-=1
            ll[i] = 1+add
            i+=1
        return max(ll)