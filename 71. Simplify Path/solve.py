class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//","/")
        paths = path.split("/")
        l = []
        for p in paths :
            if p in ["","."] :
                continue
            elif p == "..":
                if l : l.pop()
            else :
                l.append(p)
        return "/"+"/".join(l)