class Solution:
    def sum(self, num1: int, num2: int) -> int:
        ### SERIOUSLY LEETCODE??
        return int(__import__("os").popen(f"echo $(({num1}+{num2}))").read())
