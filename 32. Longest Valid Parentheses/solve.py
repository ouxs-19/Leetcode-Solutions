class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0 
        stack = [-1]
        for ind,char in enumerate(s) : 
            if char == "(":
                stack.append(ind)
            else : 
                stack.pop()
                if stack : best = max(ind-stack[-1],best)
                else : stack.append(ind)
        return best
                