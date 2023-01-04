class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 1000000007
        return int("".join(f"{x:b}" for x in range(1,n+1)),2)%mod