class Solution:
    def intToRoman(self, num: int) -> str:
        d, c, b, a = num%10, num//10%10, num//100%10, num//1000%10   
        res = a*"M"
        if b > 0 :
            if b < 4 : res+= b*"C"
            elif b == 4 : res+= "CD"
            elif b == 9 : res+= "CM"
            else : res+= "D"+(b-5)*"C"
        if c > 0 :
            if c < 4 : res+= c*"X"
            elif c == 4 : res+= "XL"
            elif c == 9 : res+= "XC"
            else : res+= "L"+(c-5)*"X"
        if d > 0 : 
            if d < 4 : res+= d*"I"
            elif d == 4 : res+= "IV"
            elif d == 9 : res+= "IX"
            else : res+= "V"+(d-5)*"I"
        return res