class Solution:
    def generate(self, n: int) -> List[List[int]]:
        rows = []
        if n >= 1 : rows.append([1])
        if n >= 2 : rows.append([1,1])
        for j in range(n-2):
            l = rows[-1]
            res = [1]
            for i in range(len(l)-1):
                res.append(l[i]+l[i+1])
            res.append(1)
            rows.append(res)
        return rows