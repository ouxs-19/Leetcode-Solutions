class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isReachable(self, s, d):
        visited =[False]*(self.V)
        queue=[]
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            if n == d:
                   return True
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        g = Graph()
        vals = {}
        cnt = 0 
        for eq in equations:
            a,*op,b = eq
            if op[0] == "=" and a != b:
                if a not in vals :
                    vals[a] = cnt
                    cnt+=1
                if b not in vals : 
                    vals[b] = cnt
                    cnt+=1
                g.addEdge(vals[a],vals[b])
                g.addEdge(vals[b],vals[a])
        g.V = cnt   
        for eq in equations:
            a,*op,b = eq
            if op[0] == "!":
                if a == b :
                    return False 
                if a not in vals or b not in vals : 
                    continue 
                if g.isReachable(vals[a],vals[b]):
                    return False 
        return True