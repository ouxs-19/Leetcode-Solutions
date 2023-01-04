class Solution(object):
    def isPalindrome(self, s):
        new_s = ""
        for char in s :
            if char.isalpha():
                new_s += char.lower()
            elif char.isdigit():
                new_s += char
                
        return new_s == new_s[::-1] 
        