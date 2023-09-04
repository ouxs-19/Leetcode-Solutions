class Solution:
    def minimumOperations(self, num: str) -> int:
        num = [c for c in num]
        n = len(num)
        
        def count(i,cnt,k):
            if i == -1 : 
                if k == 2 : return n
                return cnt
            if k == 0:
                if num[i] == "0":
                    return min(count(i-1,cnt+1,k),count(i-1,cnt,k+1))
                elif num[i] == "5":
                    return min(count(i-1,cnt+1,k),count(i-1,cnt,k+2))
                else:
                    return count(i-1,cnt+1,k)
                    
            if k == 1:
                if num[i] in ["5","0"]:
                    return cnt
                else:
                    return count(i-1,cnt+1,k)
                     
            if k == 2:
                if num[i] in ["2","7"]:
                    return cnt
                else:
                    return count(i-1,cnt+1,k)          
        
        return count(n-1,0,0)