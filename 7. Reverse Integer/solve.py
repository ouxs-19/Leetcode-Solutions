class Solution(object):
    def reverse(self, x):
        x = str(x)
        x = int(x[::-1]) if "-" not in x else int("-"+x[:0:-1])
        if x > 2147483647 or x < -2147483648 :
            return 0
        else : 
            return x