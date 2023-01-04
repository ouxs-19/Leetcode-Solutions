class Solution(object):
    def longestOnes(self, arr, k):
        i ,j = 0 , 0 
        n = len(arr)
        longest = k 
        while j<n :
            if arr[j] == 1 :
                j+=1
            else :
                if k>0 :
                    j+=1
                    k-=1
                elif k == 0 :
                    longest = max(longest,j-i)
                    while arr[i] != 0 :
                        i+=1
                    i+=1
                    k+=1
        longest = max(longest,j-i)
        return longest