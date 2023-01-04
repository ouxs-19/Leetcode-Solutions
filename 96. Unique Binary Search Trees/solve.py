class Solution(object):
    def numTrees(self, n):
        if n == 0 :
            return 1 
        return int((2*(2*(n-1)+1)*self.numTrees(n-1))/(n+1))