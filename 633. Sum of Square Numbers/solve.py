from math import sqrt 
class Solution(object):
    def judgeSquareSum(self, c):
        l = int(sqrt(c))
        for i in range(l+1):
            b = sqrt(c-i**2)
            if (b - int(b)) == 0 : return True 
        return False 