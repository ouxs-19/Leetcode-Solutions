# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a,b = 1,n 
        while True : 
            c = (a+b) // 2 
            res = guess(c)
            if res == 0 :
                return c 
            elif res == 1 :
                a = c +1 
            else :
                b = c-1