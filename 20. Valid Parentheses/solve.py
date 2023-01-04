class Solution:
    def isValid(self, s: str) -> bool:
        ops = []
        comp = {"{":"}","(":")","[":"]"}
        for op in s :
            if op in "([{":
                ops.append(op)
            else :
                if ops : 
                    cond = ops.pop()
                    if op != comp[cond] : return False 
                else : return False 
        return not ops