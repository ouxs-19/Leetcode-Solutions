class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i, j  = 0, 0 
        boundries = [i,j]
        while i< len(s):
            if s[i] not in dic :
                dic[s[i]] = i
                i+=1
            else :
                if (i-j) > (boundries[1]-boundries[0]):
                    boundries = [j,i]
                j  = dic[s[i]] + 1
                i = j 
                dic = {}
        if (i-j)> (boundries[1]-boundries[0]):
            boundries = [j,i]
        return (boundries[1]-boundries[0])