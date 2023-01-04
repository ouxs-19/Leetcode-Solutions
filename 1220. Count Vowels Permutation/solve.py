class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = {"":["a","e","i","o","u"],"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"]}
        @cache
        def solve(i,last):
            if i == n : 
                return 1 
            return sum(solve(i+1,v) for v in vowels[last])
        return solve(0, "") % 1000000007