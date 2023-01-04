class Solution(object):
    def divide(self, dividend, divisor):
        d = dividend//divisor
        sign = 1 if dividend*divisor >0 else -1
        res= sign*(abs(dividend) // abs(divisor)) 
        if res > 2147483647 :
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res
