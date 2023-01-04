class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m = len(strs), len(strs[0])
        delete = 0
        for j in range(m):
            i = 1
            flag = 0
            while i < n:
                if strs[i][j] < strs[i-1][j]:
                    flag = 1
                    break
                i += 1
            if flag : 
                delete += 1
        
        return delete