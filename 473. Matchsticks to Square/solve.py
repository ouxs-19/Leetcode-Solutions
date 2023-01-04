class Solution:
    def makesquare(self, s: List[int]) -> bool:
        l = sum(s)/4
        if int(l) != l or (ln:=len(s)) < 4 : return False 
        new = [0 for _ in range(4)]
        s.sort(reverse=True)

        def solve(i):
            if i == ln : 
                return new[0] == new[1] == new[3] == l 
            for j in range(4):
                if new[j] + s[i] <= l : 
                    new[j]+=s[i]
                    if solve(i+1) : return True 
                    new[j]-=s[i] 
                    if not new[j]  : break
            return False 
        return solve(0)