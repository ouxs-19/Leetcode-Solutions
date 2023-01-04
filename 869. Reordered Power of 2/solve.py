class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for cand in itertools.permutations(str(n)) : 
            if cand[0] != "0" and bin(int("".join(cand))).count("1") == 1 : 
                return True
        return False 