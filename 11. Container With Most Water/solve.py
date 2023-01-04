class Solution(object):
    def maxArea(self, height):
        i = 0 
        j = len(height)-1
        s = 0 
        while i<j : 
            s = max(s,(j-i)*min(height[i],height[j]))
            if height[i] > height[j]:
                j-=1
            else :
                i+=1
        return s 