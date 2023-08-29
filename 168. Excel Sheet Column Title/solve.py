class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        power = 26
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        column = ""

        while columnNumber > 0 :
            columnNumber-=1
            coeff = columnNumber % power
            column =  chars[coeff] + column
            columnNumber  = columnNumber  // power 

        return column