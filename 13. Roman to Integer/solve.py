from collections import Counter
class Solution:
    def romanToInt(self, s: str) -> int:
        score = 0 
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if "IV" in s : 
            s = s.replace("IV","")
            score +=4
        if "IX" in s : 
            s = s.replace("IX","")
            score +=9
        if "XL" in s : 
            s = s.replace("XL","")
            score +=40
        if "XC" in s : 
            s = s.replace("XC","")
            score +=90
        if "CD" in s : 
            s = s.replace("CD","")
            score +=400
        if "CM" in s : 
            s = s.replace("CM","")
            score +=900
        c = Counter(s)
        for char in c :
            score += dic[char]*c[char]
        return score