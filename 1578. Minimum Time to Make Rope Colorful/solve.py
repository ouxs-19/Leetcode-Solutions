class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        s  = 0
        sm = 0
        ind, l = 0, len(colors)
        while ind<l :
            clr = colors[ind]
            mn = neededTime[ind]
            sm = mn 
            while ind<l-1 and colors[ind+1] == clr:
                mn = max(mn,neededTime[ind+1])
                sm += neededTime[ind+1]
                ind+=1
            s += (sm-mn)
            ind+=1
        return s 