class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = sorted(Counter(arr).values())
        cnt = 0
        size,goal = len(arr), len(arr)//2 
        while size > goal : 
            size-=c.pop()
            cnt+=1
        return cnt 