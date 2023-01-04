import string 

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        valid = string.digits
        mul = 1
        num = ""
        if s : 
            if s[0] in valid or s[0] == "-" or s[0]=="+" : 
                if s[0] == "-":
                    mul = -1 
                    if len(s) > 1 and s[1] in valid :
                        n = len(s)
                        i = 1 
                        while i<n and s[i] in valid : 
                            num+=s[i]
                            i+=1
                    else : return 0
                elif s[0] == "+":
                    if len(s) > 1 and s[1] in valid :
                        n = len(s)
                        i = 1 
                        while i<n and s[i] in valid : 
                            num+=s[i]
                            i+=1
                    else : return 0
                else :
                    n = len(s)
                    i = 0 
                    while i<n and s[i] in valid : 
                        num+=s[i]
                        i+=1
            else : return 0
        else : return 0
        num = int(num)*mul
        if num > 2147483647 : return 2147483647
        if num < -2147483648 : return -2147483648
        return num