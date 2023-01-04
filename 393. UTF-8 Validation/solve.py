class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0
        for d in data : 
            bn = bin(int(d))[2:].rjust(8,"0")
            if not need : 
                if bn.startswith("0"):
                    continue 
                elif bn.startswith("110") :
                    need = 1
                elif bn.startswith("1110") :
                    need = 2 
                elif bn.startswith("11110") : 
                    need = 3 
                else : 
                    return False 
            else : 
                if bn.startswith("10"):
                    need -= 1
                else : 
                    return False 
        return not need 