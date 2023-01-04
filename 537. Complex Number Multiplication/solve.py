class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split("+")
        c,d = num2.split("+")        
        b = b[:-1]
        d = d[:-1]
        a , b = int(a)*int(c)-int(b)*int(d) , int(a)*int(d)+int(b)*int(c)
        return f"{a}+{b}i"