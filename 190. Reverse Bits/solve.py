class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:b}".rjust(32,'0')[::-1],2)