from functools import *

class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def calc(n):
            if n == 0 : return 0
            if n <= 2 : return 1 
            return calc(n-1)+calc(n-2)
        return calc(n)